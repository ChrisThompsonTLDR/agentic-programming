#!/usr/bin/env python3
"""
Headless SDLC Orchestrator - Main Entry Point

A Python-based system that parses Markdown-based agent definitions
and orchestrates them as autonomous agents.
"""
import argparse
import sys
from pathlib import Path

from orchestrator.markdown_parser import MarkdownParser
from orchestrator.agent_factory import AgentFactory
from orchestrator.guardrail_supervisor import GuardrailSupervisor
from orchestrator.pipeline_controller import PipelineController


def get_repo_root() -> Path:
    """Get the repository root directory."""
    return Path(__file__).parent


def main():
    """Main entry point for the orchestrator."""
    parser = argparse.ArgumentParser(
        description="Headless SDLC Orchestrator - Transform markdown agents into autonomous executors"
    )
    
    parser.add_argument(
        "goal",
        nargs="?",
        help="User goal for the epic (e.g., 'Create a user authentication system')"
    )
    
    parser.add_argument(
        "--phase",
        choices=["Foundation", "Planning", "Role Definition", "Process", "Development", "Finalization"],
        default="Foundation",
        help="Starting phase for execution (default: Foundation)"
    )
    
    parser.add_argument(
        "--command",
        help="Execute a single command by number (e.g., '22' for architect)"
    )
    
    parser.add_argument(
        "--list-agents",
        action="store_true",
        help="List all available agents"
    )
    
    parser.add_argument(
        "--show-pipeline",
        action="store_true",
        help="Display the pipeline structure"
    )
    
    parser.add_argument(
        "--commands-dir",
        type=Path,
        help="Path to commands directory (default: ./commands)"
    )
    
    parser.add_argument(
        "--forbidden-file",
        type=Path,
        help="Path to forbidden.md file (default: ./support/01-forbidden.md)"
    )
    
    args = parser.parse_args()
    
    # Determine paths
    repo_root = get_repo_root()
    commands_dir = args.commands_dir or repo_root / "commands"
    forbidden_file = args.forbidden_file or repo_root / "support" / "01-forbidden.md"
    
    # Validate paths
    if not commands_dir.exists():
        print(f"Error: Commands directory not found: {commands_dir}")
        sys.exit(1)
    
    if not forbidden_file.exists():
        print(f"Error: Forbidden file not found: {forbidden_file}")
        sys.exit(1)
    
    # Initialize components
    print("Initializing Headless SDLC Orchestrator...")
    print(f"Commands directory: {commands_dir}")
    print(f"Forbidden rules: {forbidden_file}\n")
    
    md_parser = MarkdownParser(commands_dir)
    guardrail_supervisor = GuardrailSupervisor(forbidden_file)
    agent_factory = AgentFactory(md_parser)
    
    # Load guardrails into factory
    agent_factory.load_guardrails(forbidden_file)
    
    pipeline_controller = PipelineController(agent_factory, guardrail_supervisor)
    
    # Handle different modes
    if args.show_pipeline:
        pipeline_controller.display_pipeline_structure()
        return
    
    if args.list_agents:
        list_all_agents(md_parser)
        return
    
    if args.command:
        execute_single_command(args.command, args.goal, agent_factory)
        return
    
    # Full pipeline execution
    if not args.goal:
        print("Error: Please provide a goal for the epic")
        print("\nUsage examples:")
        print("  python main.py 'Create user authentication system'")
        print("  python main.py 'Add payment processing' --phase Planning")
        print("  python main.py --command 22 'Design the data architecture'")
        print("  python main.py --list-agents")
        print("  python main.py --show-pipeline")
        sys.exit(1)
    
    # Execute the pipeline
    print(f"\nExecuting pipeline with goal: {args.goal}")
    print(f"Starting from phase: {args.phase}\n")
    
    result = pipeline_controller.execute_full_pipeline(args.goal, args.phase)
    
    # Display summary
    display_execution_summary(result)


def list_all_agents(md_parser):
    """List all available agents organized by phase."""
    print("\n" + "="*70)
    print("AVAILABLE AGENTS")
    print("="*70 + "\n")
    
    phases = md_parser.get_commands_by_phase()
    
    for phase_name in ["Foundation", "Planning", "Role Definition", "Process", "Development", "Finalization"]:
        if phase_name in phases:
            print(f"\n{phase_name}:")
            print("-" * 70)
            
            for agent_def in phases[phase_name]:
                cmd_num = agent_def.get("command_number", "??")
                title = agent_def.get("title", "Unknown")
                filepath = agent_def.get("filepath", "")
                
                print(f"  [{cmd_num}] {title}")
                print(f"      File: {Path(filepath).relative_to(Path(filepath).parent.parent.parent)}")
    
    print("\n" + "="*70 + "\n")


def execute_single_command(command_number: str, goal: str, agent_factory):
    """Execute a single command/agent."""
    if not goal:
        goal = f"Execute command {command_number}"
    
    print(f"\nExecuting single command: {command_number}")
    print(f"Goal: {goal}\n")
    
    agent = agent_factory.create_agent(command_number)
    
    if not agent:
        print(f"Error: Agent not found for command number: {command_number}")
        print("\nUse --list-agents to see available commands")
        sys.exit(1)
    
    result = agent.execute(goal)
    
    print("\n" + "="*70)
    print("EXECUTION RESULT")
    print("="*70)
    print(f"Status: {result['status']}")
    print(f"Agent: [{result['agent']}] {result['title']}")
    print(f"Phase: {result['phase']}")
    
    if result['status'] == 'success':
        print(f"\nOutput:\n{result['output']}")
    else:
        print(f"\nReason: {result.get('reason', 'Unknown')}")
    
    print("="*70 + "\n")


def display_execution_summary(result):
    """Display a summary of pipeline execution."""
    print("\n" + "#"*70)
    print("# EXECUTION SUMMARY")
    print("#"*70 + "\n")
    
    print(f"Goal: {result['goal']}")
    print(f"Status: {result['status']}")
    print(f"Phases Executed: {len(result['phases_executed'])}")
    print(f"Total Commands: {len(result['history'])}\n")
    
    print("Phase Results:")
    print("-" * 70)
    
    for phase_name, phase_result in result['results'].items():
        status = phase_result.get('status', 'unknown')
        status_icon = "✓" if status == "success" else "✗"
        
        print(f"{status_icon} {phase_name}: {status}")
        
        if 'results' in phase_result:
            for cmd_result in phase_result['results']:
                cmd_status = cmd_result.get('status', 'unknown')
                cmd_icon = "✓" if cmd_status == "success" else "✗"
                title = cmd_result.get('title', 'Unknown')
                agent_num = cmd_result.get('agent', '??')
                
                print(f"  {cmd_icon} [{agent_num}] {title}")
    
    print("\n" + "#"*70 + "\n")


if __name__ == "__main__":
    main()
