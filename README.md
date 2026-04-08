# Agentic Programming

A collection of custom GitHub Copilot Cloud Agents for research and documentation.

## Agents

| Agent | Trigger | Output |
|-------|---------|--------|
| `laravel-package` | `/laravel-package <vendor/package>` | `.steering/laravel-packages/<vendor>__<package>.md` |
| `skill-research` | `/skill-research <github-url-to-skill>` | `.steering/skills/<owner>__<skill-name>.md` |
| `mcp-research` | `/mcp-research <url>` | `mcps/<owner>__<name>.md` |

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

## File Structure

```
.github/
├── agents/
│   ├── laravel-package.agent.md       # Laravel package agent
│   └── skill-research.agent.md        # Skill research agent
├── skills/
│   ├── laravel-research/
│   │   ├── SKILL.md                   # Note generator skill
│   │   └── laravel-package-template.md  # Blank template reference
│   └── skill-research/
│       ├── SKILL.md                   # Skill note generator skill
│       └── skill-template.md          # Blank template reference
└── workflows/
    └── copilot-setup-steps.yml        # Environment setup

.steering/
├── laravel-packages/                  # Laravel package research notes
│   └── <vendor>__<package>.md
└── skills/                            # Copilot skill research notes
    └── <owner>__<skill-name>.md
```

---

## Skill Research Agent

A custom GitHub Copilot Cloud Agent that researches GitHub Copilot skills and generates structured research notes.

### Usage

In Copilot Chat (GitHub.com, VS Code, or JetBrains), select the `skill-research` agent and prompt:

```
/skill-research https://github.com/microsoft/skills/blob/main/.github/skills/copilot-sdk
```

The agent will research the skill and write a note to:

```
.steering/skills/microsoft__copilot-sdk.md
```

### How It Works

1. Parses the GitHub URL to extract `owner`, `repo`, `path`, and `skill-name`.
2. Researches via GitHub MCP and DeepWiki:
   - Reads `SKILL.md` for description and capabilities.
   - Lists all files in the skill directory.
   - Searches for agents/workflows that use the skill.
   - Reads the parent repo README for ecosystem context.
3. Generates a structured note using the skill template.
4. Writes the note to `.steering/skills/<owner>__<skill-name>.md`.
