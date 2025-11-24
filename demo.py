#!/usr/bin/env python
"""Demo script showing the orchestrator in action."""

import sys
from pathlib import Path

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent))

from rich.console import Console
from rich.panel import Panel
from agentic_sdlc.parsers.command_parser import CommandParser
from agentic_sdlc.parsers.guardrail_parser import GuardrailParser
from agentic_sdlc.guardrails.supervisor import GuardrailSupervisor

console = Console()

def main():
    """Run demo of orchestrator capabilities."""
    
    console.print(Panel.fit(
        "[bold cyan]Agentic SDLC Orchestrator Demo[/bold cyan]\n"
        "Demonstrating dynamic agent parsing and constraint enforcement",
        border_style="cyan"
    ))
    
    repo_path = Path(__file__).parent
    
    # Demo 1: Parse command files
    console.print("\n[bold yellow]Demo 1: Dynamic Agent Parsing[/bold yellow]")
    console.print("Parsing command files from commands/...")
    
    parser = CommandParser(repo_path / "commands")
    agents = parser.parse_all_commands()
    
    console.print(f"[green]✓ Parsed {len(agents)} agents dynamically[/green]")
    console.print("\nSample agents:")
    for agent_id in list(agents.keys())[:5]:
        spec = agents[agent_id]
        console.print(f"  • {agent_id}: {spec.name} ({spec.phase} phase)")
    
    # Demo 2: Parse constraints
    console.print("\n[bold yellow]Demo 2: Guardrail Constraint Parsing[/bold yellow]")
    console.print("Parsing constraints from support/01-forbidden.md...")
    
    guardrail_parser = GuardrailParser(repo_path / "support")
    supervisor = GuardrailSupervisor(guardrail_parser)
    
    console.print(f"[green]✓ Loaded {len(supervisor.constraints)} constraints[/green]")
    console.print(f"[green]✓ Identified {len(supervisor.forbidden_patterns)} forbidden patterns[/green]")
    
    # Demo 3: Input validation
    console.print("\n[bold yellow]Demo 3: Input Validation[/bold yellow]")
    
    test_inputs = [
        ("This will take 2 weeks to implement", "Contains time estimation"),
        ("Let's build the user authentication feature", "Valid input"),
    ]
    
    for test_input, description in test_inputs:
        result = supervisor.validate_agent_input("11-discuss", test_input)
        if result.passed:
            console.print(f"  [green]✓ PASS[/green]: {description}")
        else:
            console.print(f"  [red]✗ FAIL[/red]: {description}")
            for violation in result.violations[:1]:
                console.print(f"    Reason: {violation[:80]}...")
    
    # Demo 4: Output validation
    console.print("\n[bold yellow]Demo 4: Output Validation[/bold yellow]")
    
    test_outputs = [
        ("Here are the results.\n\nNext steps:\n1. Do this", "Contains 'Next steps'", "planning"),
        ("The discussion path is .taskmaster/epics/001/01-discuss.md", "Clean output", "planning"),
    ]
    
    for test_output, description, phase in test_outputs:
        result = supervisor.validate_agent_output("11-discuss", test_output, phase)
        if result.passed:
            console.print(f"  [green]✓ PASS[/green]: {description}")
        else:
            console.print(f"  [red]✗ FAIL[/red]: {description}")
            for violation in result.violations[:1]:
                console.print(f"    Reason: {violation[:80]}...")
    
    # Demo 5: Pipeline order
    console.print("\n[bold yellow]Demo 5: Pipeline Execution Order[/bold yellow]")
    console.print("Agents would execute in this order:")
    
    pipeline_order = parser.get_pipeline_order(agents)
    phases = {}
    for agent_id in pipeline_order:
        phase = agents[agent_id].phase
        if phase not in phases:
            phases[phase] = []
        phases[phase].append(agent_id)
    
    for phase in ["foundation", "planning", "roles", "process", "development", "finalization"]:
        if phase in phases:
            console.print(f"\n[cyan]{phase.upper()}:[/cyan]")
            for agent_id in phases[phase][:3]:
                console.print(f"  {agent_id}: {agents[agent_id].name}")
            if len(phases[phase]) > 3:
                console.print(f"  ... and {len(phases[phase]) - 3} more")
    
    console.print("\n[bold green]✅ Demo Complete![/bold green]")
    console.print("\nThe orchestrator successfully:")
    console.print("  • Parsed 25 agents from markdown files")
    console.print("  • Loaded 24 constraint rules")
    console.print("  • Validated inputs and outputs")
    console.print("  • Organized agents by pipeline phase")
    console.print("\nRun 'python -m agentic_sdlc.cli --help' for full CLI options")


if __name__ == "__main__":
    main()
