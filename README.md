# Agentic Programming

A collection of custom GitHub Copilot Cloud Agents for research and documentation.

## Source of truth: `.steering`

**Agents** and **packaged skills** are authored under **`.steering/`** and mirrored into `.cursor`, `.claude`, and `.github` using the checklist in **`.steering/README.md`**.

If you edit a file under `.cursor/` or `.github/`, merge those changes back into `.steering` and replicate out again. CI (**Verify steering sync**) fails when mirrors drift.

See **`.steering/README.md`** for layout details.

## Agents

| Agent | Trigger | Output |
|-------|---------|--------|
| `idea` | `/idea <free-text idea or path to scratch file>` | `.steering/ideas/<slug>.md` |
| `laravel-package` | `/laravel-package <vendor/package>` | `.steering/laravel-packages/<vendor>__<package>.md` |
| `research-skill` | `/research-skill <url-to-skill-directory>` | `.steering/skills/<namespace>__<skill-name>.md` |
| `research-mcp` | `/research-mcp <url>` | `.steering/mcps/<owner>__<name>.md` |

---

# Laravel Package Research Agent

A custom GitHub Copilot Cloud Agent that researches Laravel packages and generates Obsidian-style research notes.

## Setup

Before using the agent, complete these two steps:

### 1. Add Secrets

Go to **Repo Settings > Secrets and variables > Copilot env** and add:

- `DEEPWIKI_KEY` — API key from [DeepWiki](https://api.deepwiki.com)
- `CONTEXT7_KEY` — API key from [Context7](https://context7.com)

### 2. Enable Memory

Go to **Repo Settings > Copilot > Memory** and enable it so the agent learns from past runs.

---

## Usage

In Copilot Chat (GitHub.com, VS Code, or JetBrains), select the `laravel-package` agent and prompt:

```
/laravel-package spatie/laravel-markdown-response
```

The agent will research the package and write a note to:

```
.steering/laravel-packages/spatie__laravel-markdown-response.md
```

## How It Works

1. Parses `<vendor/package>` from the prompt.
2. Researches via DeepWiki, GitHub MCP, and Context7:
   - GitHub repo stats (stars, forks, releases)
   - Packagist downloads
   - Laravel News article
   - Package docs
3. Generates a structured note using the Laravel package template.
4. Writes the note to `.steering/laravel-packages/<vendor>__<package>.md`.

## Configuration

### MCP Servers

Add to repo **Settings > Copilot > MCP**:

```json
{
  "mcpServers": {
    "deepwiki": {
      "type": "sse",
      "url": "https://api.deepwiki.com/sse",
      "tools": ["*"],
      "headers": { "Authorization": "Bearer $DEEPWIKI_KEY" }
    },
    "context7": {
      "command": "npx",
      "args": ["@context7/mcp-server"],
      "env": { "CONTEXT7_API_KEY": "${CONTEXT7_KEY:-fallback}" }
    },
    "github": {
      "type": "sse",
      "url": "https://mcp.github.com/sse",
      "tools": ["read", "search"]
    }
  }
}
```

### Secrets

Add to **Repo Settings > Secrets and variables > Copilot env**:

- `DEEPWIKI_KEY` — from [DeepWiki](https://api.deepwiki.com)
- `CONTEXT7_KEY` — from [Context7](https://context7.com)

### Memory

Enable in **Repo Settings > Copilot > Memory** so the agent learns from past runs.

## File Structure (summary)

```
.steering/
├── README.md                          # Steering layout & sync rules
├── agents/                            # Canonical agents → .cursor / .claude / .github
├── skills/                            # Packaged skills (subdirs) + research notes (flat *.md)
├── templates/                         # AGENTS.md, agent.md, skill.md (skill spec)
├── laravel-packages/                  # Laravel research notes
│   └── <vendor>__<package>.md
├── mcps/                              # MCP server research notes
│   └── <owner>__<name>.md
└── ...

.github/
├── agents/                            # Mirrored from .steering/agents/
├── skills/                            # Mirrored packaged skills + skill-research extras
└── workflows/
    └── verify-steering-sync.yml       # CI: script + git diff --exit-code

.cursor/  .claude/                     # Mirrored agents & skills (see .steering/README.md)
```

---

## Skill Research Agent

A custom GitHub Copilot Cloud Agent that researches **agent skills** published in git repositories (from a URL you provide) and writes structured research notes.

### Usage

In Copilot Chat (GitHub.com, VS Code, or JetBrains), select the `research-skill` agent and prompt with a URL to a skill directory in a git host (for example a repository folder view or equivalent):

```
/research-skill https://example.com/org/repo/tree/main/path/to/skill
```

The agent will write a research note to:

```
.steering/skills/<namespace>__<skill-name>.md
```

### How It Works

1. Parses the URL to identify host, repository coordinates, and path to the skill directory.
2. Researches using live tools (repository access when available, plus DeepWiki, Context7, etc.).
3. Reads the skill’s `SKILL.md` and related files.
4. Generates a structured note using the repo’s skill template (see `.steering/templates/skill.md` and mirrored `skill-template` files).
5. Writes the note under `.steering/skills/`.
