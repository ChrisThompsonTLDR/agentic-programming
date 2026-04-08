---
name: agentic-programming
description: Context about the agentic-programming repo setup, configuration, and required secrets.
---
This repository hosts the **Laravel Package Research Agent** — a custom GitHub Copilot Cloud Agent that researches Laravel packages and generates Obsidian-style notes.

## Required Setup

### 1. Add Secrets

Go to **Repo Settings > Secrets and variables > Copilot env** and add:

| Secret | Description |
|--------|-------------|
| `DEEPWIKI_KEY` | API key from [DeepWiki](https://api.deepwiki.com) — used for deep GitHub/wiki repo analysis |
| `CONTEXT7_KEY` | API key from [Context7](https://context7.com) — used for code context and Laravel-specific patterns |

These secrets are referenced by the MCP server config in `.github/agents/laravel-package.agent.md`.

### 2. Enable Memory

Go to **Repo Settings > Copilot > Memory** and enable it.

Memory allows the agent to learn from past `/laravel-package` runs (e.g., common frontmatter patterns). Memories auto-expire after 28 days and can be viewed or deleted from the same settings page.

## Agent Usage

Select the `laravel-package` agent in Copilot Chat and prompt:

```
/laravel-package <vendor/package>
```

Example:

```
/laravel-package spatie/laravel-markdown-response
```

Output is written to `.steering/laravel-packages/<vendor>__<package>.md`.

## Key Files

| Path | Purpose |
|------|---------|
| `.github/agents/laravel-package.agent.md` | Agent profile and MCP server config |
| `.github/skills/laravel-research/SKILL.md` | Note-generator skill with package template |
| `.github/skills/laravel-research/laravel-package-template.md` | Blank template reference |
| `.steering/laravel-packages/` | Output directory for generated notes |
| `.steering/skills/` | Output directory for skill research notes |
| `mcps/` | Output directory for MCP server research notes |
