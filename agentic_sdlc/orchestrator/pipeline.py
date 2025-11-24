"""Pipeline controller for orchestrating agent workflows."""

import json
from pathlib import Path
from typing import Dict, Any, List, Optional
from dataclasses import dataclass
from enum import Enum

from openai import OpenAI

from ..parsers.command_parser import AgentSpec
from ..agents.factory import AgentFactory
from ..guardrails.supervisor import GuardrailSupervisor


class PipelinePhase(Enum):
    """Pipeline phases."""
    FOUNDATION = "foundation"
    PLANNING = "planning"
    ROLES = "roles"
    PROCESS = "process"
    DEVELOPMENT = "development"
    FINALIZATION = "finalization"
    OPERATIONS = "operations"


@dataclass
class PipelineState:
    """Current state of the pipeline."""
    
    epic_id: Optional[str]
    epic_title: Optional[str]
    current_phase: PipelinePhase
    current_agent_id: Optional[str]
    completed_agents: List[str]
    artifacts: Dict[str, str]  # agent_id -> artifact_path
    context: Dict[str, Any]  # Shared context between agents


class PipelineController:
    """Orchestrates the 5-phase workflow and manages agent handoffs."""
    
    PHASE_ORDER = [
        PipelinePhase.FOUNDATION,
        PipelinePhase.PLANNING,
        PipelinePhase.ROLES,
        PipelinePhase.PROCESS,
        PipelinePhase.DEVELOPMENT,
        PipelinePhase.FINALIZATION,
    ]
    
    def __init__(
        self,
        client: OpenAI,
        agent_factory: AgentFactory,
        supervisor: GuardrailSupervisor,
        agent_specs: Dict[str, AgentSpec],
        project_root: Path,
    ):
        """Initialize pipeline controller."""
        self.client = client
        self.agent_factory = agent_factory
        self.supervisor = supervisor
        self.agent_specs = agent_specs
        self.project_root = Path(project_root)
        
        # Create all agents
        self.agents = agent_factory.create_all_agents(agent_specs)
        
        # Group agents by phase
        self.agents_by_phase = self._group_agents_by_phase()
        
        # Initialize state
        self.state = PipelineState(
            epic_id=None,
            epic_title=None,
            current_phase=PipelinePhase.FOUNDATION,
            current_agent_id=None,
            completed_agents=[],
            artifacts={},
            context={},
        )
    
    def _group_agents_by_phase(self) -> Dict[PipelinePhase, List[str]]:
        """Group agents by their pipeline phase."""
        grouped = {phase: [] for phase in PipelinePhase}
        
        phase_map = {
            "foundation": PipelinePhase.FOUNDATION,
            "planning": PipelinePhase.PLANNING,
            "roles": PipelinePhase.ROLES,
            "process": PipelinePhase.PROCESS,
            "development": PipelinePhase.DEVELOPMENT,
            "finalization": PipelinePhase.FINALIZATION,
            "operations": PipelinePhase.OPERATIONS,
        }
        
        for agent_id, spec in self.agent_specs.items():
            phase = phase_map.get(spec.phase, PipelinePhase.FOUNDATION)
            grouped[phase].append(agent_id)
        
        # Sort agents within each phase by their ID
        for phase in grouped:
            grouped[phase].sort()
        
        return grouped
    
    def initialize_epic(self, epic_title: str) -> Dict[str, Any]:
        """Initialize a new epic and start the pipeline."""
        print(f"\n🚀 Initializing epic: {epic_title}")
        
        # Execute 00-start agent
        start_agent = self.agents.get("00-start")
        if not start_agent:
            raise ValueError("00-start agent not found")
        
        result = self._execute_agent(
            "00-start",
            start_agent,
            user_input=epic_title,
        )
        
        # Update state
        self.state.epic_title = epic_title
        self.state.current_phase = PipelinePhase.PLANNING
        
        return result
    
    def execute_phase(self, phase: PipelinePhase, user_inputs: Dict[str, str] = None) -> List[Dict[str, Any]]:
        """Execute all agents in a specific phase."""
        user_inputs = user_inputs or {}
        agent_ids = self.agents_by_phase.get(phase, [])
        
        print(f"\n📋 Executing {phase.value} phase with {len(agent_ids)} agents")
        
        results = []
        for agent_id in agent_ids:
            agent_config = self.agents.get(agent_id)
            if not agent_config:
                print(f"⚠️  Agent {agent_id} not found, skipping")
                continue
            
            user_input = user_inputs.get(agent_id, "")
            
            result = self._execute_agent(agent_id, agent_config, user_input)
            results.append(result)
            
            # Store artifacts
            if result.get("artifact_path"):
                self.state.artifacts[agent_id] = result["artifact_path"]
            
            # Update context
            if result.get("context"):
                self.state.context.update(result["context"])
        
        self.state.current_phase = phase
        return results
    
    def execute_full_pipeline(self, epic_title: str, interactive: bool = False) -> Dict[str, Any]:
        """Execute the complete pipeline from start to finish."""
        print(f"\n{'='*80}")
        print(f"🎯 Starting Full Pipeline Execution")
        print(f"Epic: {epic_title}")
        print(f"{'='*80}\n")
        
        # Initialize epic
        init_result = self.initialize_epic(epic_title)
        
        all_results = {
            "foundation": [init_result],
            "planning": [],
            "roles": [],
            "process": [],
            "development": [],
            "finalization": [],
        }
        
        # Execute each phase in order
        for phase in self.PHASE_ORDER[1:]:  # Skip foundation (already done)
            if interactive:
                input(f"\n⏸️  Press Enter to execute {phase.value} phase...")
            
            phase_results = self.execute_phase(phase)
            all_results[phase.value] = phase_results
        
        print(f"\n{'='*80}")
        print(f"✅ Pipeline Execution Complete")
        print(f"{'='*80}\n")
        
        return {
            "epic_title": epic_title,
            "epic_id": self.state.epic_id,
            "results": all_results,
            "artifacts": self.state.artifacts,
        }
    
    def _execute_agent(
        self,
        agent_id: str,
        agent_config: Dict[str, Any],
        user_input: str = "",
    ) -> Dict[str, Any]:
        """Execute a single agent."""
        print(f"\n🤖 Executing agent: {agent_id} ({agent_config['name']})")
        
        # Validate input
        if user_input:
            validation = self.supervisor.validate_agent_input(agent_id, user_input)
            if not validation.passed:
                print(f"❌ Input validation failed:")
                for violation in validation.violations:
                    print(f"   - {violation}")
                return {
                    "agent_id": agent_id,
                    "success": False,
                    "error": "Input validation failed",
                    "violations": validation.violations,
                }
        
        # Prepare agent context
        context = self._prepare_agent_context(agent_id)
        
        # Build prompt
        prompt = self._build_agent_prompt(agent_id, agent_config, user_input, context)
        
        try:
            # Execute agent (simulated for now - would use OpenAI Agents SDK in production)
            output = self._simulate_agent_execution(agent_id, agent_config, prompt)
            
            # Validate output
            spec = self.agent_specs.get(agent_id)
            phase = spec.phase if spec else "unknown"
            validation = self.supervisor.validate_agent_output(agent_id, output, phase)
            
            if not validation.passed:
                print(f"❌ Output validation failed:")
                for violation in validation.violations:
                    print(f"   - {violation}")
                return {
                    "agent_id": agent_id,
                    "success": False,
                    "error": "Output validation failed",
                    "violations": validation.violations,
                }
            
            if validation.warnings:
                print(f"⚠️  Warnings:")
                for warning in validation.warnings:
                    print(f"   - {warning}")
            
            # Mark as completed
            self.state.completed_agents.append(agent_id)
            
            print(f"✅ Agent {agent_id} completed successfully")
            
            return {
                "agent_id": agent_id,
                "success": True,
                "output": output,
                "warnings": validation.warnings,
            }
            
        except Exception as e:
            print(f"❌ Agent execution failed: {e}")
            return {
                "agent_id": agent_id,
                "success": False,
                "error": str(e),
            }
    
    def _prepare_agent_context(self, agent_id: str) -> Dict[str, Any]:
        """Prepare context for agent execution."""
        return {
            "epic_id": self.state.epic_id,
            "epic_title": self.state.epic_title,
            "completed_agents": self.state.completed_agents,
            "artifacts": self.state.artifacts,
            "shared_context": self.state.context,
        }
    
    def _build_agent_prompt(
        self,
        agent_id: str,
        agent_config: Dict[str, Any],
        user_input: str,
        context: Dict[str, Any],
    ) -> str:
        """Build the prompt for agent execution."""
        parts = [
            "## Epic Context",
            f"Epic: {context.get('epic_title', 'N/A')}",
            f"Epic ID: {context.get('epic_id', 'N/A')}",
            "",
        ]
        
        if context.get("artifacts"):
            parts.extend([
                "## Available Artifacts",
                "The following artifacts have been created by previous agents:",
            ])
            for prev_agent_id, artifact_path in context["artifacts"].items():
                parts.append(f"- {prev_agent_id}: {artifact_path}")
            parts.append("")
        
        if user_input:
            parts.extend([
                "## User Input",
                user_input,
                "",
            ])
        
        return "\n".join(parts)
    
    def _simulate_agent_execution(
        self,
        agent_id: str,
        agent_config: Dict[str, Any],
        prompt: str,
    ) -> str:
        """Simulate agent execution (placeholder for actual OpenAI Agents SDK call)."""
        # This is a placeholder - in production, this would use the OpenAI Agents SDK
        # to create and run the agent
        return f"Simulated output from agent {agent_id}\n\nAgent would execute based on:\n{agent_config['instructions'][:200]}..."
    
    def get_pipeline_status(self) -> Dict[str, Any]:
        """Get current pipeline status."""
        return {
            "epic_id": self.state.epic_id,
            "epic_title": self.state.epic_title,
            "current_phase": self.state.current_phase.value,
            "completed_agents": len(self.state.completed_agents),
            "total_agents": len(self.agents),
            "artifacts": len(self.state.artifacts),
        }
