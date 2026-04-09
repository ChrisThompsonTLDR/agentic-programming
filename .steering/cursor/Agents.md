---
title: Cursor Agents
url: https://cursor.com/docs/subagents
tags: [cursor, agents, subagents, task-tool]
related:
  - "[[cursor/Rules]]"
  - "[[cursor/Skills]]"
  - "[[cursor/Hooks]]"
  - "[[github-copilot/Agents]]"
---

# Cursor Agents

In Cursor’s documentation these are **subagents**—specialized assistants the **Cursor Agent** delegates to via the **Task** tool. This steering note parallels **`.steering/github-copilot/Agents.md`** (Copilot custom agents): same repo layout idea (**steering → `.cursor/agents/`**), different product surface.

**Official reference:** [Subagents | Cursor Docs](https://cursor.com/docs/subagents)

Each subagent runs in its **own context window**, returns a **final summary** to the parent, and fits **noisy or long-running work** (exploration, shell output, browser automation) without filling the main chat.

## How this repo models Cursor agents

| Layer | Role |
|--------|------|
| **Canonical source** | `.steering/agents/*.md` — edit here first. May include **GitHub Copilot–only** YAML (`tools:`, `mcp-servers:`) for `.github/agents/`. |
| **Cursor mirror** | `.cursor/agents/` — **built** from steering: template embeds under `templates/` are expanded; Copilot-only keys are **stripped** so Cursor sees `name`, `description`, and body. |
| **Claude / GitHub** | `.claude/agents/` (same strip as Cursor), `.github/agents/` (full YAML for Copilot). |

Replication rules and CI behavior are documented in **`.steering/agents/sync-agents.md`** and **`.github/workflows/verify-steering-sync.yml`**.

For **GitHub Copilot** custom agents (`.github/agents/`, `tools:`, `mcp-servers:`), see **`.steering/github-copilot/Agents.md`**.

## File locations (Cursor)

Per Cursor’s docs, custom subagents live in:

| Scope | Path |
|--------|------|
| **Project** | `.cursor/agents/` (and optionally `.claude/agents/`, `.codex/agents/` for compatibility) |
| **User** | `~/.cursor/agents/` |

Project agents override user agents when names conflict; `.cursor/` wins over `.claude/` / `.codex/` for the same name.

**This repository** keeps the **authoritative** definitions under **`.steering/agents/`** and regenerates `.cursor/agents/` so the workspace stays in sync with steering.

## File format

Each agent is a **Markdown** file with **YAML frontmatter** (first `---` … `---` block), then the **system-style prompt** for that subagent.

### Frontmatter fields (Cursor)

| Field | Required | Purpose |
|--------|----------|---------|
| `name` | No | Identifier; defaults from filename. Lowercase and hyphens are typical. |
| `description` | No | Shown in Task hints; the parent agent uses this to choose **when** to delegate. |
| `model` | No | `inherit` (default), `fast`, or a specific model ID. See [models and pricing](https://cursor.com/docs/models-and-pricing). |
| `readonly` | No | If `true`, restricted writes (no edits / state-changing shell, per product behavior). |
| `is_background` | No | If `true`, non-blocking background run. |

**Copilot-only keys** (`tools:`, `mcp-servers:`) are **not** part of Cursor’s subagent format; they live in steering for the **`.github/agents/`** mirror only and are removed for `.cursor/agents/`.

### Example (Cursor-shaped, as in this repo’s mirrors)

This matches the **stripped** shape under `.cursor/agents/` (see e.g. **`.cursor/agents/laravel-package.agent.md`**):

```yaml
---
name: laravel-package
description: "Researches Laravel packages and generates Obsidian notes. Usage: /laravel-package <vendor/package>"
---

You are a Laravel package researcher…
```

### Example (steering source with Copilot YAML)

Canonical files under **`.steering/agents/`** may include extra keys for GitHub (see **`.steering/agents/research-mcp.agent.md`**):

```yaml
---
name: research-mcp
description: "Researches an MCP server from a URL…"
tools: ["read", "search", "edit", "browser"]
---
```

After sync, **`.cursor/agents/research-mcp.agent.md`** drops `tools:` and keeps `name`, `description`, and body.

**Naming:** Cursor’s quick start uses names like `verifier.md`. This repo also uses **`.agent.md`** (e.g. `laravel-package.agent.md`) for parity with Copilot’s agent file convention; treat the **frontmatter `name`** as the stable identifier for `/name` invocation.

## Behavior (summary from Cursor docs)

- **Delegation** — The agent may spawn subagents automatically from task shape and **descriptions**, or you can invoke them with **`/subagent-name`** in the prompt.
- **Context** — Subagents do **not** see prior parent chat history; the parent must pass needed context in the task prompt.
- **Modes** — **Foreground** (wait for result) vs **background** (return immediately; resumable via agent id).
- **Built-ins** — **Explore**, **Bash**, and **Browser** are built-in subagents Cursor may use without custom files.

## Agents vs skills

Cursor positions **subagents** for isolated context, parallel workstreams, and multi-step specialization; **skills** are better for **single-shot, repeatable** actions. See [Skills](https://cursor.com/docs/skills) and **`.steering/cursor/Rules.md`** for rules/skill context.

## Related in this repo

| File | Why |
|------|-----|
| `.steering/agents/sync-agents.md` | How steering → `.cursor/agents/` build and strip works. |
| `.steering/agents/laravel-package.agent.md` | Full steering example (Copilot keys + embed). |
| `.cursor/agents/laravel-package.agent.md` | Cursor mirror after strip + embed expansion. |
| `.steering/github-copilot/Agents.md` | Copilot custom agents (cloud / VS Code). |

## Resources

- [Subagents](https://cursor.com/docs/subagents) — format, locations, model field, patterns.
- [Cloud Agents](https://cursor.com/docs/cloud-agent) — subagents in cloud workflows (Cursor docs).
- [Models and pricing](https://cursor.com/docs/models-and-pricing) — model IDs for `model:`.
