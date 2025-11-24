# Cursor Agentic Development Pipeline

A comprehensive, AI-powered software development workflow that orchestrates multiple specialized agents through a structured pipeline to deliver complete epics from conception to deployment.

## Overview

This system implements a **5-phase agentic pipeline** that transforms high-level ideas into production-ready software through coordinated AI agents. Each agent has a specialized role and operates within strict constraints to ensure quality, consistency, and traceability.

## Architecture

### Core Pipeline Structure

```
Foundation & Setup (00-03)
├── commands/00-start.md       - Initialize new epic
├── support/01-forbidden.md    - Universal constraints & guardrails
├── support/02-mcp.md          - MCP server activation
├── support/03-pipeline.md     - Pipeline orchestration
└── support/04-rules.md        - Rule loader

Planning Phase (10-17)
├── 11-discuss.md   - Product discovery
├── 12-idea.md      - Concept development
├── 13-packages.md  - Dependency analysis
├── 14-prd.md       - Requirements specification
├── 15-user-stories.md - User journey mapping
├── 16-mermaid.md   - Architecture visualization
└── 17-create.md    - Task breakdown

Role Definition (20-26)
├── 21-devops.md    - Infrastructure planning
├── 22-architect.md - System design
├── 23-backend.md   - Backend implementation
├── 24-frontend.md  - Frontend implementation
├── 25-test.md      - Testing strategy
└── 26-lead.md      - Project leadership

Process Management (30-31)
└── 31-expand.md    - Task expansion & refinement

Development Phase (40-44)
├── 41-open.md      - Development initiation
├── 42-code.md      - Implementation
├── 43-verify.md    - Quality assurance
└── 44-close.md     - Task completion

Finalization (50-54)
├── 51-docs.md      - Documentation
├── 52-qa.md        - Quality audit
├── 53-done.md      - Epic completion
└── 54-pr.md        - Pull request creation

PR Review Phase (60-64)
├── 61-review.md    - PR review analysis
├── 62-address.md   - Review feedback implementation
├── 63-verify.md    - Review changes verification
└── 64-commit.md    - Review changes commit & push

Research Phase (80-82)
├── 81-research.md  - Package research
└── 82-gap.md       - Gap analysis

Operations (99)
└── 99-rebake.md    - Re-bake epic artifacts
```

> **📖 The command files shown in the pipeline structure above correspond to the agent roles listed below. Click any command number in the agent roles section to view detailed implementation.**

## MCP Server Integrations

The system leverages multiple **Model Context Protocol (MCP) servers** for enhanced capabilities:

### 🤖 **Task Master AI** (`task-master-ai`)
Multi-provider AI orchestration supporting:
- Anthropic Claude
- OpenAI GPT
- Google Gemini
- Mistral
- Perplexity
- Groq
- Azure OpenAI
- Ollama

### 📚 **Context7** (`context7`)
- Library and documentation integration
- Real-time API references
- Framework documentation

### 🔍 **Perplexity** (`perplexity`)
- Web research and analysis
- Real-time information gathering
- Technical research capabilities

### 🌐 **DeepWiki** (`deepwiki`)
- Repository analysis and insights
- Code pattern recognition
- Best practices research

### 🛠️ **Laravel Boost** (`laravel-boost`)
- Laravel framework expertise
- PHP ecosystem knowledge
- Laravel-specific optimization

### 🧠 **Sequential Thinking** (`sequential-thinking`)
- Structured reasoning processes
- Step-by-step problem solving
- Logic validation and refinement

### 🗂️ **New Knowledge** (`knowledgegraph`)
- Knowledge graph management
- Memory and context retention
- Related information discovery

### 🐙 **GitHub** (`github`)
- GitHub integration
- Repository management
- PR and issue handling

## Agent Roles & Responsibilities

### 🎯 **Planning Phase (10-17)**
- **Product Manager** ([11-discuss](commands/10-planning/11-discuss.md)): Problem space definition and user research
- **Innovation Lead** ([12-idea](commands/10-planning/12-idea.md)): Creative solution ideation
- **Package Manager** ([13-packages](commands/10-planning/13-packages.md)): Technology stack analysis
- **Requirements Engineer** ([14-prd](commands/10-planning/14-prd.md)): Technical specification writing
- **UX Researcher** ([15-user-stories](commands/10-planning/15-user-stories.md)): User journey and story mapping
- **System Architect** ([16-mermaid](commands/10-planning/16-mermaid.md)): Visual system design
- **Project Manager** ([17-create](commands/10-planning/17-create.md)): Task decomposition and planning

### 👥 **Role Definition Phase (20-26)**
- **DevOps Engineer** ([21-devops](commands/20-roles/21-devops.md)): Infrastructure and deployment planning
- **System Architect** ([22-architect](commands/20-roles/22-architect.md)): Technical architecture design
- **Backend Developer** ([23-backend](commands/20-roles/23-backend.md)): API and data layer design
- **Frontend Developer** ([24-frontend](commands/20-roles/24-frontend.md)): User interface planning
- **QA Engineer** ([25-test](commands/20-roles/25-test.md)): Testing strategy and validation
- **Engineering Lead** ([26-lead](commands/20-roles/26-lead.md)): Technical leadership and oversight

### ⚙️ **Process Phase (30-31)**
- **Process Engineer** ([31-expand](commands/30-process/31-expand.md)): Task refinement and optimization

### 💻 **Development Phase (40-44)**
- **Development Lead** ([41-open](commands/40-dev/41-open.md)): Implementation coordination
- **Software Engineer** ([42-code](commands/40-dev/42-code.md)): Code implementation and integration
- **Quality Engineer** ([43-verify](commands/40-dev/43-verify.md)): Testing and validation
- **Release Manager** ([44-close](commands/40-dev/44-close.md)): Feature completion and handover

### 📋 **Finalization Phase (50-54)**
- **Technical Writer** ([51-docs](commands/50-final/51-docs.md)): Documentation creation
- **Quality Auditor** ([52-qa](commands/50-final/52-qa.md)): Comprehensive quality review
- **Completion Lead** ([53-done](commands/50-final/53-done.md)): Epic completion and knowledge capture
- **Integration Lead** ([54-pr](commands/50-final/54-pr.md)): Pull request and deployment preparation

### 🔀 **PR Review Phase (60-64)**
- **Code Review Engineer** ([61-review](commands/60-git/61-review.md)): PR review analysis and documentation
- **Development Engineer** ([62-address](commands/60-git/62-address.md)): Review feedback implementation
- **Quality Engineer** ([63-verify](commands/60-git/63-verify.md)): Review changes verification
- **Release Engineer** ([64-commit](commands/60-git/64-commit.md)): Review changes commit and push

### 🔬 **Research Phase (80-82)**
- **Package Research Partner** ([81-research](commands/80-research/81-research.md)): Laravel package research and evaluation
- **Gap Analysis Partner** ([82-gap](commands/80-research/82-gap.md)): Comparative analysis between solutions

### 🔄 **Operations (99)**
- **Planning Steward** ([99-rebake](commands/99-rebake.md)): Re-bake epic artifacts and harmonize existing planning

## Universal Constraints & Guardrails

All agents operate under strict **[support/01-forbidden.md](support/01-forbidden.md)** constraints:

### ✅ **Allowed Actions**
- **Truth over assumption**: All data must trace to PRD, tasks, or user input
- **Local-first operations**: All work within project workspace
- **Non-destructive changes**: No modification of unrelated components
- **MCP-orchestrated actions**: All operations through approved tools
- **Rule-based execution**: Commands must load shared rules from `support/04-rules.md`

### ❌ **Forbidden Actions**
- **Time estimation** or scope invention
- **Code generation during planning phases**
- **External dependency addition without approval**
- **Security credential exposure**
- **Unapproved documentation modification**
- **Direct manipulation** of task-master files (must use MCP tools)
- **Speculative recommendations** or "Next steps" in output

### 🎯 **Quality Gates**
- **Pint**: Code cleanliness and standards
- **Larastan**: Static analysis (level ≥6 or baseline)
- **Mutation Testing**: ≥70% coverage
- **Performance**: p95 ≤500ms, ≤10 queries
- **Error Tracking**: 0 unhandled exceptions

### 📋 **Support Files**
All commands reference these foundational files:
- `support/01-forbidden.md` - Universal constraints and guardrails
- `support/02-mcp.md` - MCP server activation and usage
- `support/03-pipeline.md` - Pipeline orchestration guide
- `support/04-rules.md` - Rule loader for epic workflows

## Getting Started

### Prerequisites
1. **Cursor** with MCP server support
2. **API Keys** for integrated services (see `mcp.json`)
3. **GitHub** repository access
4. **Laravel** project environment (optional but recommended)

### Configuration

1. **Setup MCP Servers**: Configure `mcp.json` with your API keys
2. **Review Support Files**: All commands reference `support/01-forbidden.md`, `support/02-mcp.md`, `support/03-pipeline.md`, and `support/04-rules.md`
3. **Initialize Epic**: Run `/00-start "Your Epic Title"`
4. **Follow Pipeline**: Execute commands sequentially through each phase

### Example Workflow

```bash
# Initialize new epic
00-start

# Planning phase
11-discuss
12-idea
13-packages
14-prd
15-user-stories
16-mermaid
17-create

# Role definition
21-devops
22-architect
23-backend
24-frontend
25-test
26-lead

# Process refinement
31-expand

# Development execution
41-open
42-code
43-verify
44-close

# Finalization
51-docs
52-qa
53-done
54-pr

# PR Review (when feedback received)
61-review
62-address
63-verify
64-commit

# Research (as needed)
81-research  # Package research
82-gap       # Gap analysis

# Operations (as needed)
99-rebake
```

## Key Features

### 🔄 **Automated Orchestration**
- Sequential command execution
- Context preservation across phases
- Automatic artifact generation
- Git integration and tracking

### 🎯 **Specialized Intelligence**
- Role-specific AI agents
- Multi-provider AI integration
- Contextual knowledge retention
- Research and analysis capabilities

### 🛡️ **Quality Assurance**
- Built-in constraint enforcement
- Multi-stage validation
- Comprehensive testing integration
- Performance monitoring

### 📊 **Traceability**
- Complete audit trails
- PRD-to-implementation mapping
- Task and artifact linking
- Git commit integration

## Integration Examples

### GitHub Integration
- Automatic branch creation
- PR generation with descriptions
- Issue tracking and linking
- Repository analysis

### Documentation Generation
- API documentation
- User guides
- Architecture diagrams
- Deployment guides

### Testing Integration
- Unit test generation
- Integration testing
- Performance testing
- Quality gate validation

## Advanced Features

### 🔄 **Context Management**
- Knowledge graph integration
- Memory retention across sessions
- Related epic discovery
- Pattern recognition

### 🔍 **Research Capabilities**
- Real-time web research
- Library and framework analysis
- Best practice identification
- Technical trend awareness

### 🎨 **Visualization**
- Architecture diagrams (Mermaid)
- User journey mapping
- System flow documentation
- Dependency visualization

## Contributing

This system is designed as a **complete, self-contained workflow**. Each command file represents a specific agent role and should maintain:

1. **Single responsibility** per command
2. **Clear input/output contracts**
3. **MCP tool integration**
4. **Constraint compliance** with `support/01-forbidden.md`
5. **Comprehensive documentation**

### File Structure

```
.cursor/
├── commands/          # Command implementations organized by phase
│   ├── 00-start.md
│   ├── 10-planning/
│   ├── 20-roles/
│   ├── 30-process/
│   ├── 40-dev/
│   ├── 50-final/
│   ├── 60-git/
│   ├── 80-research/
│   └── 99-rebake.md
├── support/           # Universal constraints and configuration
│   ├── 01-forbidden.md
│   ├── 02-mcp.md
│   ├── 03-pipeline.md
│   └── 04-rules.md
├── rules/             # Epic-specific rules (epics/*.mdc)
│   └── epics/
└── mcp.json           # MCP server configuration
```

## License

This agentic workflow system is designed for **Laravel ecosystem development** but can be adapted for other frameworks with appropriate MCP server configuration.

## Key Workflow Features

### 🔄 **Re-baking Epics**
The `99-rebake` command allows you to refactor and harmonize existing epic planning artifacts without creating new scope. Useful when requirements evolve or artifacts become stale.

### 📝 **Epic Completion**
The `53-done` command finalizes completed epics by:
- Synthesizing delivery summaries
- Updating epic task records
- Recording knowledge graph insights
- Marking epics as complete

## Headless SDLC Orchestrator

A **Python-based orchestrator** that transforms the markdown-based agent definitions into executable code objects. This enables programmatic automation of the SDLC pipeline.

### 🚀 **Quick Start**

```bash
# Display pipeline structure
python main.py --show-pipeline

# List all available agents
python main.py --list-agents

# Execute full pipeline
python main.py "Create user authentication system"

# Execute single agent
python main.py --command 22 "Design data architecture"

# Run examples
python examples.py
```

### 📦 **Components**

- **MarkdownParser**: Extracts agent definitions from markdown files
- **AgentFactory**: Creates agent instances with guardrails
- **GuardrailSupervisor**: Enforces constraints from `support/01-forbidden.md`
- **PipelineController**: Orchestrates workflow phases

### 📖 **Documentation**

See [orchestrator/README.md](orchestrator/README.md) for complete documentation, API reference, and integration guide.

---

**Built for Cursor** • **MCP-Powered** • **Quality-First** • **Traceable Development**
