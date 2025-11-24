#!/usr/bin/env python3
"""
Example usage demonstrations for the Headless SDLC Orchestrator.

This script shows various ways to use the orchestrator programmatically.
"""
from pathlib import Path
from orchestrator.markdown_parser import MarkdownParser
from orchestrator.agent_factory import AgentFactory
from orchestrator.guardrail_supervisor import GuardrailSupervisor
from orchestrator.pipeline_controller import PipelineController


def example_1_list_all_agents():
    """Example 1: Discover and list all available agents."""
    print("\n" + "="*70)
    print("EXAMPLE 1: Discover and List All Agents")
    print("="*70 + "\n")
    
    # Initialize parser
    commands_dir = Path(__file__).parent / "commands"
    parser = MarkdownParser(commands_dir)
    
    # Get all agents organized by phase
    phases = parser.get_commands_by_phase()
    
    print(f"Found {sum(len(agents) for agents in phases.values())} agents across {len(phases)} phases\n")
    
    for phase_name, agents in phases.items():
        print(f"{phase_name}: {len(agents)} agents")
        for agent in agents[:3]:  # Show first 3
            print(f"  - [{agent['command_number']}] {agent['title']}")
        if len(agents) > 3:
            print(f"  ... and {len(agents) - 3} more")
        print()


def example_2_inspect_agent_prompt():
    """Example 2: Extract and inspect an agent's system prompt."""
    print("\n" + "="*70)
    print("EXAMPLE 2: Extract Agent System Prompt")
    print("="*70 + "\n")
    
    commands_dir = Path(__file__).parent / "commands"
    parser = MarkdownParser(commands_dir)
    
    # Parse the architect agent (command 22)
    architect_file = commands_dir / "20-roles" / "22-architect.md"
    agent_def = parser.parse_file(architect_file)
    
    print(f"Agent: {agent_def['title']}")
    print(f"Phase: {agent_def['phase']}")
    print(f"Command: {agent_def['command_number']}")
    print(f"\nSystem Prompt (first 500 chars):")
    print("-" * 70)
    print(agent_def['system_prompt'][:500])
    print("...")
    print()


def example_3_load_guardrails():
    """Example 3: Load and inspect guardrails from forbidden.md."""
    print("\n" + "="*70)
    print("EXAMPLE 3: Load and Inspect Guardrails")
    print("="*70 + "\n")
    
    forbidden_file = Path(__file__).parent / "support" / "01-forbidden.md"
    supervisor = GuardrailSupervisor(forbidden_file)
    
    print("Global Principles:")
    for principle in supervisor.get_global_principles():
        print(f"  - {principle['name']}: {principle['description'][:60]}...")
    
    print("\nQuality Gates:")
    for gate, threshold in supervisor.get_quality_gates().items():
        print(f"  - {gate}: {threshold}")
    
    print()


def example_4_create_single_agent():
    """Example 4: Create and use a single agent."""
    print("\n" + "="*70)
    print("EXAMPLE 4: Create and Execute Single Agent")
    print("="*70 + "\n")
    
    commands_dir = Path(__file__).parent / "commands"
    forbidden_file = Path(__file__).parent / "support" / "01-forbidden.md"
    
    parser = MarkdownParser(commands_dir)
    factory = AgentFactory(parser)
    factory.load_guardrails(forbidden_file)
    
    # Create the PRD agent (command 14)
    prd_agent = factory.create_agent("14")
    
    if prd_agent:
        print(f"Created agent: {prd_agent}")
        print(f"Title: {prd_agent.title}")
        print(f"Phase: {prd_agent.phase}")
        
        # Execute with sample input
        result = prd_agent.execute(
            "Create a comprehensive PRD for user authentication",
            context={"epic_folder": "001_auth_system"}
        )
        
        print(f"\nExecution Status: {result['status']}")
        print(f"Output preview: {result['output'][:200]}...")
    else:
        print("Agent not found!")
    
    print()


def example_5_validate_action():
    """Example 5: Validate an action against guardrails."""
    print("\n" + "="*70)
    print("EXAMPLE 5: Validate Action Against Guardrails")
    print("="*70 + "\n")
    
    forbidden_file = Path(__file__).parent / "support" / "01-forbidden.md"
    supervisor = GuardrailSupervisor(forbidden_file)
    
    # Test valid action
    valid_action = {
        "type": "planning",
        "phase": "Planning",
        "content": "Define user stories based on PRD requirements"
    }
    
    result = supervisor.validate_action("planning", valid_action)
    print(f"Valid action test: {result['valid']}")
    
    # Test invalid action (contains "next steps")
    invalid_action = {
        "type": "output",
        "content": "Here are the next steps to implement..."
    }
    
    result = supervisor.validate_action("output", invalid_action)
    print(f"Invalid action test: {result['valid']}")
    if not result['valid']:
        print(f"Violations: {len(result['violations'])}")
        for v in result['violations']:
            print(f"  - {v['category']}: {v['rule'][:60]}...")
    
    print()


def example_6_phase_execution():
    """Example 6: Execute a complete workflow phase."""
    print("\n" + "="*70)
    print("EXAMPLE 6: Execute Complete Workflow Phase")
    print("="*70 + "\n")
    
    commands_dir = Path(__file__).parent / "commands"
    forbidden_file = Path(__file__).parent / "support" / "01-forbidden.md"
    
    parser = MarkdownParser(commands_dir)
    supervisor = GuardrailSupervisor(forbidden_file)
    factory = AgentFactory(parser)
    factory.load_guardrails(forbidden_file)
    
    controller = PipelineController(factory, supervisor)
    
    # Execute just the Foundation phase
    print("Executing Foundation phase...")
    result = controller.execute_phase(
        "Foundation",
        "Create a task management application",
        {"user": "developer"}
    )
    
    print(f"\nPhase Status: {result['status']}")
    print(f"Commands Executed: {len(result['results'])}")
    
    for cmd_result in result['results']:
        status_icon = "✓" if cmd_result['status'] == 'success' else "✗"
        print(f"  {status_icon} [{cmd_result['agent']}] {cmd_result['title']}")
    
    print()


def example_7_pipeline_structure():
    """Example 7: Display pipeline structure programmatically."""
    print("\n" + "="*70)
    print("EXAMPLE 7: Access Pipeline Structure")
    print("="*70 + "\n")
    
    commands_dir = Path(__file__).parent / "commands"
    forbidden_file = Path(__file__).parent / "support" / "01-forbidden.md"
    
    parser = MarkdownParser(commands_dir)
    supervisor = GuardrailSupervisor(forbidden_file)
    factory = AgentFactory(parser)
    factory.load_guardrails(forbidden_file)
    
    controller = PipelineController(factory, supervisor)
    
    print("Pipeline Phases:")
    for phase in controller.get_phase_order():
        agents = factory.get_agents_by_phase(phase)
        print(f"\n{phase}:")
        print(f"  Agents: {len(agents)}")
        print(f"  Commands: {', '.join(a.command_number for a in agents)}")
    
    print()


def example_8_custom_workflow():
    """Example 8: Create a custom workflow with selected agents."""
    print("\n" + "="*70)
    print("EXAMPLE 8: Custom Workflow with Selected Agents")
    print("="*70 + "\n")
    
    commands_dir = Path(__file__).parent / "commands"
    forbidden_file = Path(__file__).parent / "support" / "01-forbidden.md"
    
    parser = MarkdownParser(commands_dir)
    factory = AgentFactory(parser)
    factory.load_guardrails(forbidden_file)
    
    # Custom workflow: just planning essentials
    custom_workflow = ["00", "14", "15", "17"]  # Start, PRD, Stories, Create
    
    print("Custom workflow agents:")
    for cmd in custom_workflow:
        agent = factory.create_agent(cmd)
        if agent:
            print(f"  [{agent.command_number}] {agent.title}")
    
    print("\nExecuting custom workflow...")
    context = {}
    for cmd in custom_workflow:
        agent = factory.create_agent(cmd)
        if agent:
            result = agent.execute(
                "Build API for mobile app",
                context
            )
            context[f"step_{cmd}"] = result['output']
            print(f"  ✓ Completed: {agent.title}")
    
    print(f"\nWorkflow complete. Context keys: {len(context)}")
    print()


def main():
    """Run all examples."""
    print("\n" + "#"*70)
    print("# HEADLESS SDLC ORCHESTRATOR - USAGE EXAMPLES")
    print("#"*70)
    
    examples = [
        example_1_list_all_agents,
        example_2_inspect_agent_prompt,
        example_3_load_guardrails,
        example_4_create_single_agent,
        example_5_validate_action,
        example_6_phase_execution,
        example_7_pipeline_structure,
        example_8_custom_workflow,
    ]
    
    for i, example in enumerate(examples, 1):
        print(f"\n{'='*70}")
        print(f"Running Example {i}/{len(examples)}")
        print('='*70)
        try:
            example()
        except Exception as e:
            print(f"Example failed with error: {e}")
            import traceback
            traceback.print_exc()
    
    print("\n" + "#"*70)
    print("# ALL EXAMPLES COMPLETE")
    print("#"*70 + "\n")


if __name__ == "__main__":
    main()
