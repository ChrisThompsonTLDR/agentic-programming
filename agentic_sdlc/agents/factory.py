"""Agent factory for dynamic agent creation."""

from typing import Dict, Any, Optional
from openai import OpenAI

from ..parsers.command_parser import AgentSpec
from ..guardrails.supervisor import GuardrailSupervisor
from ..mcp.integration import MCPIntegration


class AgentFactory:
    """Factory for creating specialized agents from command specifications."""
    
    def __init__(
        self,
        client: OpenAI,
        guardrail_supervisor: GuardrailSupervisor,
        mcp_integration: MCPIntegration,
    ):
        """Initialize agent factory."""
        self.client = client
        self.supervisor = guardrail_supervisor
        self.mcp = mcp_integration
        
    def create_agent(self, spec: AgentSpec, model: str = "gpt-4o") -> Dict[str, Any]:
        """Create an agent from a command specification."""
        # Get constraints for this agent
        constraints_prompt = self.supervisor.format_constraints_for_prompt(
            spec.id, spec.phase
        )
        
        # Get available MCP functions for this agent
        tools = self.mcp.get_functions_for_agent(spec.id, spec.phase)
        
        # Build agent instructions
        instructions = self._build_instructions(spec, constraints_prompt)
        
        # Create agent configuration
        agent_config = {
            "name": spec.name,
            "instructions": instructions,
            "tools": tools,
            "model": model,
            "metadata": {
                "agent_id": spec.id,
                "phase": spec.phase,
                "phase_number": spec.phase_number,
            }
        }
        
        return agent_config
    
    def _build_instructions(self, spec: AgentSpec, constraints: str) -> str:
        """Build comprehensive agent instructions."""
        parts = [
            f"# {spec.name}",
            "",
            "## Your Role",
            spec.role,
            "",
            "## Context",
            f"You are operating in the {spec.phase} phase of a structured SDLC pipeline.",
            f"Your agent ID is: {spec.id}",
            "",
        ]
        
        if spec.preparation:
            parts.extend([
                "## Preparation",
                "Before executing your tasks, you must:",
            ])
            for i, prep in enumerate(spec.preparation, 1):
                parts.append(f"{i}. {prep}")
            parts.append("")
        
        if spec.steps:
            parts.extend([
                "## Execution Steps",
                "Follow these steps in order:",
            ])
            for i, step in enumerate(spec.steps, 1):
                parts.append(f"{i}. {step}")
            parts.append("")
        
        parts.extend([
            "",
            constraints,
            "",
            "## Important Notes",
            "- Always read support/01-forbidden.md, support/02-mcp.md, support/03-pipeline.md, and support/04-rules.md",
            "- Use MCP tools for all orchestration and data access",
            "- Maintain traceability to PRD and task metadata",
            "- Follow the exact output format specified in your steps",
            "- Do not add unsolicited recommendations or next steps",
        ])
        
        return "\n".join(parts)
    
    def create_all_agents(self, specs: Dict[str, AgentSpec]) -> Dict[str, Dict[str, Any]]:
        """Create all agents from specifications."""
        agents = {}
        
        for agent_id, spec in specs.items():
            agents[agent_id] = self.create_agent(spec)
        
        return agents
