"""
PipelineController - Manages workflow phases and agent orchestration.
"""
from typing import Dict, Any, List, Optional
from pathlib import Path


class PipelineController:
    """Controls the execution flow through workflow phases."""
    
    def __init__(self, agent_factory, guardrail_supervisor):
        """
        Initialize the PipelineController.
        
        Args:
            agent_factory: AgentFactory instance for creating agents
            guardrail_supervisor: GuardrailSupervisor for validation
        """
        self.agent_factory = agent_factory
        self.guardrail_supervisor = guardrail_supervisor
        self.current_phase = "Foundation"
        self.execution_history = []
        self.context = {}
        
        # Define phase structure based on repository organization
        self.phase_definitions = {
            "Foundation": {
                "commands": ["00"],
                "description": "Initialize new epic and setup workspace"
            },
            "Planning": {
                "commands": ["11", "12", "13", "14", "15", "16", "17"],
                "description": "Product discovery, requirements, and planning"
            },
            "Role Definition": {
                "commands": ["21", "22", "23", "24", "25", "26"],
                "description": "Specialized role planning and architecture"
            },
            "Process": {
                "commands": ["31"],
                "description": "Task expansion and refinement"
            },
            "Development": {
                "commands": ["41", "42", "43", "44"],
                "description": "Implementation and verification"
            },
            "Finalization": {
                "commands": ["51", "52", "53", "54"],
                "description": "Documentation, QA, and completion"
            }
        }
    
    def get_phase_order(self) -> List[str]:
        """Get the ordered list of phases."""
        return list(self.phase_definitions.keys())
    
    def get_current_phase(self) -> str:
        """Get the current workflow phase."""
        return self.current_phase
    
    def set_phase(self, phase_name: str) -> bool:
        """
        Set the current phase.
        
        Args:
            phase_name: Name of the phase to set
            
        Returns:
            True if phase was set successfully
        """
        if phase_name not in self.phase_definitions:
            print(f"Error: Unknown phase '{phase_name}'")
            return False
            
        # Validate phase transition
        validation = self.guardrail_supervisor.validate_phase_transition(
            self.current_phase,
            phase_name,
            self.context
        )
        
        if not validation["valid"]:
            print(f"Error: Phase transition blocked: {validation['reason']}")
            return False
            
        self.current_phase = phase_name
        return True
    
    def execute_phase(self, phase_name: str, user_goal: str, phase_context: Dict = None) -> Dict[str, Any]:
        """
        Execute all commands in a phase.
        
        Args:
            phase_name: Name of the phase to execute
            user_goal: User's goal or input for the phase
            phase_context: Additional context for the phase
            
        Returns:
            Dictionary with phase execution results
        """
        if phase_name not in self.phase_definitions:
            return {
                "status": "error",
                "message": f"Unknown phase: {phase_name}"
            }
        
        # Set the current phase
        if not self.set_phase(phase_name):
            return {
                "status": "error",
                "message": f"Cannot transition to phase: {phase_name}"
            }
        
        phase_def = self.phase_definitions[phase_name]
        command_numbers = phase_def["commands"]
        
        print(f"\n{'='*70}")
        print(f"EXECUTING PHASE: {phase_name}")
        print(f"Description: {phase_def['description']}")
        print(f"Commands: {', '.join(command_numbers)}")
        print(f"{'='*70}\n")
        
        phase_results = []
        phase_context = phase_context or {}
        
        # Merge phase context with global context
        execution_context = {**self.context, **phase_context}
        
        for cmd_num in command_numbers:
            result = self.execute_command(cmd_num, user_goal, execution_context)
            phase_results.append(result)
            
            # Update context with results
            if result["status"] == "success":
                execution_context[f"cmd_{cmd_num}_output"] = result["output"]
        
        # Update global context
        self.context.update(execution_context)
        
        return {
            "status": "success",
            "phase": phase_name,
            "results": phase_results,
            "context": execution_context
        }
    
    def execute_command(self, command_number: str, user_input: str, context: Dict = None) -> Dict[str, Any]:
        """
        Execute a single command/agent.
        
        Args:
            command_number: Command number to execute
            user_input: User input for the command
            context: Execution context
            
        Returns:
            Dictionary with command execution result
        """
        agent = self.agent_factory.create_agent(command_number)
        
        if not agent:
            return {
                "status": "error",
                "message": f"Agent not found for command: {command_number}"
            }
        
        # Execute the agent
        result = agent.execute(user_input, context or {})
        
        # Record in history
        self.execution_history.append({
            "command": command_number,
            "phase": agent.phase,
            "title": agent.title,
            "result": result
        })
        
        return result
    
    def execute_full_pipeline(self, user_goal: str, start_phase: str = "Foundation") -> Dict[str, Any]:
        """
        Execute the complete pipeline from start to finish.
        
        Args:
            user_goal: User's overall goal for the epic
            start_phase: Phase to start from (default: Foundation)
            
        Returns:
            Dictionary with complete pipeline execution results
        """
        print(f"\n{'#'*70}")
        print(f"# SDLC PIPELINE EXECUTION")
        print(f"# Goal: {user_goal}")
        print(f"# Starting Phase: {start_phase}")
        print(f"{'#'*70}\n")
        
        phase_order = self.get_phase_order()
        
        # Find starting index
        try:
            start_idx = phase_order.index(start_phase)
        except ValueError:
            return {
                "status": "error",
                "message": f"Invalid start phase: {start_phase}"
            }
        
        pipeline_results = {}
        
        for phase in phase_order[start_idx:]:
            phase_result = self.execute_phase(phase, user_goal)
            pipeline_results[phase] = phase_result
            
            if phase_result["status"] != "success":
                print(f"\n⚠ Pipeline halted at phase: {phase}")
                break
        
        print(f"\n{'#'*70}")
        print(f"# PIPELINE EXECUTION COMPLETE")
        print(f"{'#'*70}\n")
        
        return {
            "status": "complete",
            "goal": user_goal,
            "phases_executed": list(pipeline_results.keys()),
            "results": pipeline_results,
            "history": self.execution_history
        }
    
    def get_execution_history(self) -> List[Dict]:
        """Get the history of executed commands."""
        return self.execution_history
    
    def get_context(self) -> Dict[str, Any]:
        """Get the current execution context."""
        return self.context
    
    def display_pipeline_structure(self):
        """Display the complete pipeline structure."""
        print("\n" + "="*70)
        print("SDLC PIPELINE STRUCTURE")
        print("="*70 + "\n")
        
        for i, (phase_name, phase_def) in enumerate(self.phase_definitions.items(), 1):
            print(f"{i}. {phase_name}")
            print(f"   Description: {phase_def['description']}")
            print(f"   Commands: {', '.join(phase_def['commands'])}")
            
            # Show agents in this phase
            agents = self.agent_factory.get_agents_by_phase(phase_name)
            if agents:
                print(f"   Agents:")
                for agent in agents:
                    print(f"     - [{agent.command_number}] {agent.title}")
            print()
    
    def get_next_phase(self) -> Optional[str]:
        """Get the next phase in the pipeline."""
        phase_order = self.get_phase_order()
        
        try:
            current_idx = phase_order.index(self.current_phase)
            if current_idx + 1 < len(phase_order):
                return phase_order[current_idx + 1]
        except ValueError:
            pass
            
        return None
    
    def is_pipeline_complete(self) -> bool:
        """Check if the pipeline has completed all phases."""
        return self.current_phase == "Finalization"
