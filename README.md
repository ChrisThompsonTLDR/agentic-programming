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
│   └── laravel-package.agent.md       # Agent profile
├── skills/
│   └── laravel-research/
│       ├── SKILL.md                   # Note generator skill
│       └── laravel-package-template.md  # Blank template reference
└── workflows/
    └── copilot-setup-steps.yml        # Environment setup

.steering/
└── laravel-packages/                  # Generated research notes
    └── <vendor>__<package>.md
```
