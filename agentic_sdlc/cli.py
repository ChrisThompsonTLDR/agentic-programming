"""CLI tool for the Agentic SDLC Orchestrator."""

import json
import click
from pathlib import Path
from rich.console import Console
from rich.table import Table
from rich.panel import Panel
from rich.progress import Progress
from openai import OpenAI

from .parsers.command_parser import CommandParser
from .parsers.guardrail_parser import GuardrailParser
from .guardrails.supervisor import GuardrailSupervisor
from .mcp.integration import MCPIntegration
from .agents.factory import AgentFactory
from .orchestrator.pipeline import PipelineController


console = Console()


@click.group()
@click.version_option(version="0.1.0")
def main():
    """Agentic SDLC Orchestrator - Autonomous software development pipeline."""
    pass


@main.command()
@click.option(
    "--repo-path",
    type=click.Path(exists=True, path_type=Path),
    default=".",
    help="Path to the agentic-programming repository",
)
def list_agents(repo_path: Path):
    """List all available agents parsed from command files."""
    console.print("\n[bold cyan]Parsing command files...[/bold cyan]")
    
    commands_dir = repo_path / "commands"
    parser = CommandParser(commands_dir)
    agents = parser.parse_all_commands()
    
    # Group by phase
    phases = {}
    for agent_id, spec in agents.items():
        if spec.phase not in phases:
            phases[spec.phase] = []
        phases[spec.phase].append(spec)
    
    # Display table
    table = Table(title="Available Agents", show_header=True)
    table.add_column("ID", style="cyan")
    table.add_column("Name", style="green")
    table.add_column("Phase", style="yellow")
    
    for phase in sorted(phases.keys()):
        for spec in sorted(phases[phase], key=lambda x: x.id):
            table.add_row(spec.id, spec.name, spec.phase)
    
    console.print(table)
    console.print(f"\n[bold green]Total agents: {len(agents)}[/bold green]")


@main.command()
@click.option(
    "--repo-path",
    type=click.Path(exists=True, path_type=Path),
    default=".",
    help="Path to the agentic-programming repository",
)
def list_constraints(repo_path: Path):
    """List all constraints from support files."""
    console.print("\n[bold cyan]Parsing constraint files...[/bold cyan]")
    
    support_dir = repo_path / "support"
    parser = GuardrailParser(support_dir)
    constraints = parser.get_all_constraints()
    
    # Group by type and category
    forbidden = [c for c in constraints if c.type == "forbidden"]
    required = [c for c in constraints if c.type == "required"]
    
    # Display forbidden actions
    if forbidden:
        console.print("\n[bold red]Forbidden Actions:[/bold red]")
        for constraint in forbidden:
            severity_color = "red" if constraint.severity == "critical" else "yellow"
            console.print(f"  [{severity_color}]❌ {constraint.description}[/{severity_color}]")
    
    # Display required actions
    if required:
        console.print("\n[bold green]Required Actions:[/bold green]")
        for constraint in required:
            console.print(f"  [green]✅ {constraint.description}[/green]")
    
    console.print(f"\n[bold]Total constraints: {len(constraints)}[/bold]")


@main.command()
@click.argument("epic_title")
@click.option(
    "--repo-path",
    type=click.Path(exists=True, path_type=Path),
    default=".",
    help="Path to the agentic-programming repository",
)
@click.option(
    "--interactive/--no-interactive",
    default=False,
    help="Pause between phases for user review",
)
@click.option(
    "--api-key",
    envvar="OPENAI_API_KEY",
    help="OpenAI API key (or set OPENAI_API_KEY env var)",
)
@click.option(
    "--model",
    default="gpt-4o",
    help="OpenAI model to use for agents",
)
def execute(epic_title: str, repo_path: Path, interactive: bool, api_key: str, model: str):
    """Execute a complete epic through the pipeline."""
    if not api_key:
        console.print("[bold red]Error: OpenAI API key required[/bold red]")
        console.print("Set OPENAI_API_KEY environment variable or use --api-key option")
        return
    
    console.print(Panel.fit(
        f"[bold cyan]Executing Epic:[/bold cyan] {epic_title}",
        border_style="cyan"
    ))
    
    # Initialize components
    commands_dir = repo_path / "commands"
    support_dir = repo_path / "support"
    mcp_config_file = repo_path / "mcp.json"
    
    # Parse command files
    console.print("\n[cyan]📖 Parsing command files...[/cyan]")
    command_parser = CommandParser(commands_dir)
    agent_specs = command_parser.parse_all_commands()
    console.print(f"[green]✓ Loaded {len(agent_specs)} agent specifications[/green]")
    
    # Parse constraints
    console.print("\n[cyan]🛡️  Parsing constraints...[/cyan]")
    guardrail_parser = GuardrailParser(support_dir)
    supervisor = GuardrailSupervisor(guardrail_parser)
    console.print(f"[green]✓ Loaded {len(supervisor.constraints)} constraints[/green]")
    
    # Load MCP configuration
    console.print("\n[cyan]🔌 Loading MCP configuration...[/cyan]")
    if mcp_config_file.exists():
        mcp_config = json.loads(mcp_config_file.read_text())
    else:
        mcp_config = {"mcpServers": {}}
    mcp_integration = MCPIntegration(mcp_config)
    console.print(f"[green]✓ Loaded {len(mcp_integration.enabled_servers)} MCP servers[/green]")
    
    # Initialize OpenAI client
    console.print("\n[cyan]🤖 Initializing OpenAI client...[/cyan]")
    client = OpenAI(api_key=api_key)
    console.print(f"[green]✓ Using model: {model}[/green]")
    
    # Create agent factory
    console.print("\n[cyan]🏭 Creating agent factory...[/cyan]")
    agent_factory = AgentFactory(client, supervisor, mcp_integration)
    console.print(f"[green]✓ Agent factory ready[/green]")
    
    # Create pipeline controller
    console.print("\n[cyan]⚙️  Initializing pipeline controller...[/cyan]")
    pipeline = PipelineController(
        client=client,
        agent_factory=agent_factory,
        supervisor=supervisor,
        agent_specs=agent_specs,
        project_root=repo_path,
    )
    console.print(f"[green]✓ Pipeline ready with {len(pipeline.agents)} agents[/green]")
    
    # Execute pipeline
    console.print("\n[bold yellow]" + "="*80 + "[/bold yellow]")
    console.print("[bold yellow]Starting Pipeline Execution[/bold yellow]")
    console.print("[bold yellow]" + "="*80 + "[/bold yellow]\n")
    
    try:
        result = pipeline.execute_full_pipeline(epic_title, interactive=interactive)
        
        # Display results
        console.print("\n[bold green]" + "="*80 + "[/bold green]")
        console.print("[bold green]✅ Pipeline Execution Complete[/bold green]")
        console.print("[bold green]" + "="*80 + "[/bold green]\n")
        
        console.print(f"[bold]Epic:[/bold] {result['epic_title']}")
        console.print(f"[bold]Epic ID:[/bold] {result.get('epic_id', 'N/A')}")
        console.print(f"[bold]Artifacts Created:[/bold] {len(result['artifacts'])}")
        
        if result['artifacts']:
            console.print("\n[bold]Artifacts:[/bold]")
            for agent_id, artifact_path in result['artifacts'].items():
                console.print(f"  • {agent_id}: {artifact_path}")
        
    except Exception as e:
        console.print(f"\n[bold red]❌ Pipeline execution failed:[/bold red] {e}")
        raise


@main.command()
@click.option(
    "--repo-path",
    type=click.Path(exists=True, path_type=Path),
    default=".",
    help="Path to the agentic-programming repository",
)
def validate(repo_path: Path):
    """Validate repository structure and configuration."""
    console.print("\n[bold cyan]Validating repository...[/bold cyan]")
    
    errors = []
    warnings = []
    
    # Check directories
    required_dirs = ["commands", "support"]
    for dir_name in required_dirs:
        dir_path = repo_path / dir_name
        if not dir_path.exists():
            errors.append(f"Missing required directory: {dir_name}")
        else:
            console.print(f"[green]✓ Found {dir_name}/[/green]")
    
    # Check support files
    required_files = [
        "support/01-forbidden.md",
        "support/02-mcp.md",
        "support/03-pipeline.md",
        "support/04-rules.md",
    ]
    for file_path in required_files:
        full_path = repo_path / file_path
        if not full_path.exists():
            errors.append(f"Missing required file: {file_path}")
        else:
            console.print(f"[green]✓ Found {file_path}[/green]")
    
    # Check MCP configuration
    mcp_config = repo_path / "mcp.json"
    if not mcp_config.exists():
        warnings.append("mcp.json not found - MCP integration will be limited")
    else:
        console.print(f"[green]✓ Found mcp.json[/green]")
        try:
            config = json.loads(mcp_config.read_text())
            if "mcpServers" in config:
                console.print(f"[green]  - {len(config['mcpServers'])} MCP servers configured[/green]")
        except json.JSONDecodeError:
            errors.append("mcp.json is not valid JSON")
    
    # Parse command files
    commands_dir = repo_path / "commands"
    if commands_dir.exists():
        parser = CommandParser(commands_dir)
        agents = parser.parse_all_commands()
        console.print(f"[green]✓ Parsed {len(agents)} agent specifications[/green]")
    
    # Display results
    console.print()
    if errors:
        console.print("[bold red]Errors:[/bold red]")
        for error in errors:
            console.print(f"  [red]❌ {error}[/red]")
    
    if warnings:
        console.print("[bold yellow]Warnings:[/bold yellow]")
        for warning in warnings:
            console.print(f"  [yellow]⚠️  {warning}[/yellow]")
    
    if not errors and not warnings:
        console.print("[bold green]✅ Repository validation passed![/bold green]")
    elif not errors:
        console.print("[bold yellow]⚠️  Repository validation passed with warnings[/bold yellow]")
    else:
        console.print("[bold red]❌ Repository validation failed[/bold red]")
        return 1
    
    return 0


if __name__ == "__main__":
    main()
