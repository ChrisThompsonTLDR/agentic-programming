# Headless SDLC Orchestrator

A Python-based system that parses the Markdown-based agent definitions in this repository and orchestrates them as autonomous agents using the OpenAI Agents SDK structure.

## Overview

This orchestrator transforms the static markdown command files in the `commands/` directory into active code objects that can be executed programmatically. It demonstrates how the agentic workflow can be automated and integrated into CI/CD pipelines or custom tooling.

## Architecture

### Components

1. **MarkdownParser** (`orchestrator/markdown_parser.py`)
   - Parses markdown files from `commands/` directory
   - Extracts system prompts, role definitions, and step instructions
   - Organizes agents by workflow phase

2. **AgentFactory** (`orchestrator/agent_factory.py`)
   - Creates agent instances from parsed markdown definitions
   - Loads and applies guardrails from `support/01-forbidden.md`
   - Provides agent discovery and instantiation

3. **GuardrailSupervisor** (`orchestrator/guardrail_supervisor.py`)
   - Enforces constraints from `support/01-forbidden.md`
   - Validates agent actions and phase transitions
   - Maintains quality gate thresholds

4. **PipelineController** (`orchestrator/pipeline_controller.py`)
   - Orchestrates workflow phases in correct order
   - Manages execution context and history
   - Controls phase transitions with validation

5. **Main Entry Point** (`main.py`)
   - Command-line interface for the orchestrator
   - Supports full pipeline or single command execution
   - Provides agent listing and pipeline visualization

## Workflow Phases

The orchestrator follows the SDLC pipeline structure defined in the repository:

```
Foundation (00)
  ↓
Planning (10-17)
  ↓
Role Definition (20-26)
  ↓
Process (30-31)
  ↓
Development (40-44)
  ↓
Finalization (50-54)
```

Each phase contains specialized agents that execute specific tasks:

- **Foundation**: Initialize new epic (`00-start.md`)
- **Planning**: Product discovery, requirements, architecture (`11-discuss.md` through `17-create.md`)
- **Role Definition**: DevOps, Architect, Backend, Frontend, Test, Lead (`21-devops.md` through `26-lead.md`)
- **Process**: Task expansion and refinement (`31-expand.md`)
- **Development**: Open, Code, Verify, Close (`41-open.md` through `44-close.md`)
- **Finalization**: Docs, QA, Done, PR (`51-docs.md` through `54-pr.md`)

## Installation

### Prerequisites

- Python 3.8 or higher
- Access to the repository structure

### Setup

```bash
# Install dependencies (currently none required for basic functionality)
pip install -r requirements.txt

# Make main.py executable (optional)
chmod +x main.py
```

## Usage

### Display Pipeline Structure

```bash
python main.py --show-pipeline
```

This displays the complete SDLC pipeline with all phases and agents.

### List All Agents

```bash
python main.py --list-agents
```

Shows all available agents organized by phase.

### Execute Full Pipeline

```bash
python main.py "Create a user authentication system"
```

Executes the complete SDLC pipeline from Foundation to Finalization with the given goal.

### Start from Specific Phase

```bash
python main.py "Add payment processing" --phase Planning
```

Starts execution from the Planning phase instead of Foundation.

### Execute Single Command

```bash
python main.py --command 22 "Design the data architecture"
```

Executes only the architect agent (command 22) with the given goal.

## Examples

### Example 1: Full Pipeline Execution

```bash
python main.py "Build an inventory management system"
```

This will:
1. Initialize the epic (Foundation)
2. Run all planning agents (Planning)
3. Execute role-specific planning (Role Definition)
4. Expand tasks (Process)
5. Implement features (Development)
6. Generate docs and complete (Finalization)

### Example 2: Single Agent Execution

```bash
# Execute the architect role
python main.py --command 22 "Design data model for inventory system"

# Execute the PRD creation
python main.py --command 14 "Create requirements document"

# Execute backend developer role
python main.py --command 23 "Plan backend API structure"
```

### Example 3: Phase-by-Phase Execution

```bash
# Run foundation
python main.py "E-commerce platform" --phase Foundation

# Run planning
python main.py "E-commerce platform" --phase Planning

# Run role definition
python main.py "E-commerce platform" --phase "Role Definition"
```

## Integration with OpenAI Agents SDK

This is a **functional scaffold** demonstrating the architecture. In a production environment:

1. **Add OpenAI SDK**: Uncomment OpenAI dependencies in `requirements.txt`

2. **Configure API Keys**: Set up environment variables
   ```bash
   export OPENAI_API_KEY="your-key-here"
   ```

3. **Update Agent Execution**: Modify `Agent.execute()` in `agent_factory.py` to use real OpenAI API calls:
   ```python
   import openai
   
   response = openai.Agent.create(
       model="gpt-4",
       instructions=self.system_prompt,
       messages=[{"role": "user", "content": user_input}],
       tools=[...]  # MCP tools configuration
   )
   ```

4. **Add MCP Tools**: Configure Model Context Protocol tools based on `mcp.json`

## Guardrails and Constraints

The orchestrator automatically enforces all constraints from `support/01-forbidden.md`:

- **No scope invention**: Agents cannot create requirements without user input
- **No time estimation**: Prevents unauthorized timeline creation
- **Phase validation**: Ensures proper workflow progression
- **Security checks**: Validates against credential exposure
- **Quality gates**: Enforces metrics (Pint, Larastan, etc.)

## Extending the Orchestrator

### Adding Custom Agents

1. Create a new markdown file in appropriate `commands/` subdirectory
2. Follow the standard structure (Role & Mindset, Preparation, Steps)
3. The orchestrator will automatically discover and parse it

### Custom Guardrails

1. Update `support/01-forbidden.md` with new constraints
2. GuardrailSupervisor will automatically load them
3. Implement validation logic in `_check_violation()` if needed

### New Workflow Phases

1. Update `phase_definitions` in `PipelineController`
2. Add corresponding command files in `commands/`
3. Update phase order validation

## Development

### Project Structure

```
.
├── main.py                          # CLI entry point
├── requirements.txt                  # Dependencies
├── orchestrator/                     # Core orchestrator package
│   ├── __init__.py
│   ├── markdown_parser.py           # MD to agent definition
│   ├── agent_factory.py             # Agent instantiation
│   ├── guardrail_supervisor.py      # Constraint enforcement
│   └── pipeline_controller.py       # Workflow orchestration
├── commands/                         # Agent definitions (existing)
│   ├── 00-start.md
│   ├── 10-planning/
│   ├── 20-roles/
│   ├── 30-process/
│   ├── 40-dev/
│   └── 50-final/
└── support/                          # Constraints and config (existing)
    └── 01-forbidden.md
```

### Running Tests

```bash
# Test markdown parsing
python -c "from orchestrator.markdown_parser import MarkdownParser; \
           from pathlib import Path; \
           p = MarkdownParser(Path('commands')); \
           print(len(p.parse_all_commands()), 'agents loaded')"

# Test guardrail loading
python -c "from orchestrator.guardrail_supervisor import GuardrailSupervisor; \
           from pathlib import Path; \
           g = GuardrailSupervisor(Path('support/01-forbidden.md')); \
           print('Guardrails:', g.get_quality_gates())"
```

## Limitations

This is a **demonstration scaffold** showing how to transform markdown agents into executable code. Current limitations:

- **Simulated Execution**: Agents don't actually call LLMs (placeholder logic)
- **No MCP Integration**: MCP tools referenced in markdown are not connected
- **No State Persistence**: Context is in-memory only
- **No Error Recovery**: Limited error handling for production use

## Future Enhancements

Potential improvements for production use:

1. **Real LLM Integration**: Connect to OpenAI, Anthropic, or other providers
2. **MCP Tool Loading**: Dynamic tool registration from `mcp.json`
3. **State Persistence**: Save context to disk or database
4. **Parallel Execution**: Run independent agents concurrently
5. **Monitoring**: Add logging, metrics, and observability
6. **Configuration**: Environment-based settings (dev/staging/prod)
7. **Testing**: Unit and integration test suite

## Contributing

This orchestrator is designed to complement the markdown-based agentic workflow. When adding features:

1. Maintain compatibility with existing markdown structure
2. Follow the guardrails defined in `support/01-forbidden.md`
3. Keep the orchestrator stateless where possible
4. Document any new dependencies

## License

This orchestrator follows the same license as the parent repository.

---

**Note**: This is a functional scaffold demonstrating the architecture for parsing markdown agents and orchestrating them programmatically. It uses hypothetical OpenAI SDK patterns since actual API calls cannot be made in this environment.
