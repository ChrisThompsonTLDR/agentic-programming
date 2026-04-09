---
title: Copilot prompt files (VS Code)
url: https://code.visualstudio.com/docs/copilot/customization/prompt-files
tags:
  - github-copilot
  - vscode
  - prompt-files
  - slash-commands
related:
  - "[[github-copilot/Agents]]"
  - "[[github-copilot/Skills]]"
  - "[[github-copilot/Memories]]"
---

# Copilot prompt files in VS Code

**Official reference:** [Use prompt files in VS Code](https://code.visualstudio.com/docs/copilot/customization/prompt-files)

**Prompt files** (also called **slash commands**) are **Markdown** templates you **invoke manually** in Copilot Chat—unlike [custom instructions](https://code.visualstudio.com/docs/copilot/customization/custom-instructions), which apply **automatically**. Each file bundles **task-specific context** and **how** the model should work (steps, constraints, links to repo docs).

Use them to:

- Standardize recurring chat tasks (scaffold a component, run/fix tests, prep a PR).
- **Override** behavior for a one-off run (e.g. force **Ask** mode, a specific **model**, or a narrower **tool** list) while still using a [custom agent](https://code.visualstudio.com/docs/copilot/customization/custom-agents) for everything else.

## Prompts vs agents vs skills

From Microsoft’s guidance:

| Mechanism | When to use |
|-----------|-------------|
| **Prompt files** | **Lightweight, single-task** prompts you trigger with **`/`**. |
| **Custom agents** | **Persistent persona**, tool boundaries, handoffs (see **`.steering/github-copilot/Agents.md`**). |
| **Agent skills** | **Portable, multi-file** capability with scripts/resources (see **`.steering/github-copilot/Skills.md`**). |

**Discovery:** [Chat Customizations editor](https://code.visualstudio.com/docs/copilot/customization/overview#_chat-customizations-editor) (Preview) — Command Palette: **Chat: Open Chat Customizations**.

## Where prompt files live

| Scope | Default location |
|--------|-------------------|
| **Workspace** | **`.github/prompts/`** |
| **User (profile)** | VS Code user data for the active profile (not in the repo) |

- Extra workspace search paths: **`chat.promptFilesLocations`**.
- **Monorepos:** **`chat.useCustomizationsInParentRepositories`** pulls customizations from a **parent** repo root; see [Parent repository discovery](https://code.visualstudio.com/docs/copilot/customization/overview#_parent-repository-discovery).

**This repository** does not currently include a **`.github/prompts/`** folder; add one when you want **team-shared** slash commands in VS Code.

## File format

- Extension: **`.prompt.md`**
- Optional **YAML frontmatter** + Markdown **body** (instructions, bullet requirements, links).

### Frontmatter fields

| Field | Required | Purpose |
|--------|----------|---------|
| `description` | No | Short summary of the prompt. |
| `name` | No | Slash name after **`/`**; defaults from **filename** if omitted. |
| `argument-hint` | No | Hint text in the chat input for arguments. |
| `agent` | No | `ask`, `agent`, `plan`, or a **custom agent** name. Default: current chat agent. If **`tools`** is set, default agent is typically **`agent`**. |
| `model` | No | Model for this run; default: chat model picker. |
| `tools` | No | Allowed tools (built-in, tool sets, MCP, extension tools). MCP server wildcard: pattern like `server /*` (see [agent tools](https://code.visualstudio.com/docs/copilot/agents/agent-tools)). Unavailable tools are **ignored**. |

### Body conventions

- **Markdown links** with **relative paths** to pull in workspace context from nearby docs.
- **`#tool:toolId`** to mention tools inline (e.g. `#tool:browser`).
- **User input:** `vscode/askQuestions`, or placeholders like **`${input:variableName}`** / **`${input:variableName:placeholder}`**.
- Built-in variables such as **`${selection}`** (see VS Code doc).

Official examples (React form, security review) live on the [prompt files](https://code.visualstudio.com/docs/copilot/customization/prompt-files) page; more samples: [awesome-copilot](https://github.com/github/awesome-copilot/tree/main).

## Creating and editing

- Chat: **`/prompts`** → Configure Prompt Files.
- **Chat** view → **Configure Chat** (gear) → **Chat Customizations** → **Prompts** → **New Prompt (Workspace / User)**.
- Command Palette: **Chat: New Prompt File** / **Chat: New Untitled Prompt File**.
- **AI-assisted:** **`/create-prompt`** in chat, or **Generate Prompt** in the customizations editor; you can also ask to **turn this conversation into a reusable prompt**.

## Running a prompt

- Type **`/`** + prompt name (alongside [agent skills](https://code.visualstudio.com/docs/copilot/customization/agent-skills) slash entries).
- Pass args in the input, e.g. **`/my-prompt formName=MyForm`**.
- Command Palette: **Chat: Run Prompt**.
- Open the **`.prompt.md`** file → **Run** (play) in the editor title bar (current or new chat).

**Recommendations:** **`chat.promptFilesRecommendations`** can surface prompts when starting a new chat.

## Tool list priority

When both agents and prompts define tools:

1. **Tools** on the **prompt file** (if any)
2. Tools from the **custom agent** referenced by **`agent:`** (if any)
3. **Default** tools for the active agent mode

## Syncing user prompts

User-level prompt files can sync across machines via [Settings Sync](https://code.visualstudio.com/docs/configure/settings-sync); enable **Prompts and Instructions** in **Settings Sync: Configure**.

## Effective prompts (summary)

- State **goal** and **output shape** clearly; add **input/output examples** when helpful.
- **Link** to shared instructions instead of duplicating long policy.
- Use **`${selection}`** / **`${input:…}`** for reuse.
- Iterate with the editor **Run** button.

## Troubleshooting

- **Chat: Configure Prompt Files** — hover a prompt to see **source** (built-in, user, workspace, extension).
- Chat → right-click → **Diagnostics**; see [Troubleshooting Copilot in VS Code](https://code.visualstudio.com/docs/copilot/troubleshooting).

## Related in this repo

| File | Why |
|------|-----|
| `.steering/github-copilot/Agents.md` | Custom agents vs one-shot prompt files. |
| `.steering/github-copilot/Skills.md` | Copilot **Skills** vs prompts. |
| `.cursor/skills/` / `.steering/skills/` | Cursor **skills** use **`SKILL.md`** and a different discovery model; compare when supporting both VS Code and Cursor. |

## Resources

- [Prompt files](https://code.visualstudio.com/docs/copilot/customization/prompt-files)
- [Custom instructions](https://code.visualstudio.com/docs/copilot/customization/custom-instructions)
- [Custom agents](https://code.visualstudio.com/docs/copilot/customization/custom-agents)
- [Agent skills (VS Code)](https://code.visualstudio.com/docs/copilot/customization/agent-skills)
- [Agent tools](https://code.visualstudio.com/docs/copilot/agents/agent-tools)
- [Chat customization overview](https://code.visualstudio.com/docs/copilot/customization/overview)
- [awesome-copilot](https://github.com/github/awesome-copilot)
