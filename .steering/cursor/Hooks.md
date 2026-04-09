---
title: Cursor Hooks
url: https://cursor.com/docs/hooks
tags: [cursor, hooks, agent-loop, stdio, governance]
related:
  - "[[cursor/Agents]]"
  - "[[cursor/Rules]]"
  - "[[cursor/Skills]]"
---

# Cursor Hooks

**Official reference:** [Hooks | Cursor Docs](https://cursor.com/docs/hooks)

Hooks are **separate processes** Cursor runs at fixed points in the **agent loop** (and, with different events, for **Tab**). They talk to Cursor over **stdio** with **JSON** in both directions: they can **observe**, **block**, or **modify** behavior (format after edits, audit events, gate shells/MCP, inject session context, control **subagent / Task** execution, and more).

Third-party hook configs (e.g. Claude Code) are discussed under [Third-party hooks](https://cursor.com/docs/reference/third-party-hooks).

## How this repo relates to hooks

| Topic | In this repository |
|--------|---------------------|
| **Config location** | Project hooks: **`.cursor/hooks.json`**. Scripts typically live under **`.cursor/hooks/`** (paths in JSON are relative to the **project root**). |
| **Steering** | This note lives under **`.steering/cursor/`** so the team has a **single place** to read how hooks work; it does **not** replace Cursor reading **`.cursor/hooks.json`** at runtime. |
| **Committed hooks** | There is **no** `hooks.json` in this repo today. Add one under **`.cursor/`** when you want team-shared behavior; document new hooks here or in a short `README` next to the scripts. |
| **Cloud Agents** | Per Cursor’s docs, **project** hooks committed under **`.cursor/hooks.json`** can run in **Cloud Agents**; team/enterprise-managed hooks do **not** yet. |

For **who receives injected context** from hooks vs **subagent** boundaries, see **`.steering/cursor/Agents.md`** (subagents and the Task tool).

## Where hooks live

| Scope | Config | Scripts (typical) |
|--------|--------|-------------------|
| **Project** | `.cursor/hooks.json` | `.cursor/hooks/*.sh` (or `node`/`bun`/`python`, etc.) |
| **User (global)** | `~/.cursor/hooks.json` | `~/.cursor/hooks/*` |

Cursor **reloads** hook config when those files change.

**Path rule:** Docs often show `./hooks/...` for **user** hooks (cwd `~/.cursor/`). For **project** hooks, use **`.cursor/hooks/...`** because the process cwd is the **repository root**.

## Config shape (minimal)

```json
{
  "version": 1,
  "hooks": {
    "afterFileEdit": [{ "command": ".cursor/hooks/format.sh" }]
  }
}
```

Each event maps to an array of hook entries. Entries can be **command-based** (default) or **prompt-based** (LLM-evaluated policy).

## Hook kinds

### Command-based (default)

- **stdin:** JSON payload for the event.
- **stdout:** JSON response (when the hook mutates or signals permission).
- **Exit code:** `0` = success (use stdout JSON); `2` = **block** (same as denying in JSON); other = hook failure, action usually **proceeds** (fail-open unless docs say otherwise for your version).

Optional fields on an entry include **`timeout`**, **`matcher`** (e.g. filter shell commands), and **`type`** for non-default behaviors.

### Prompt-based

Set `"type": "prompt"` with a **`prompt`** string; Cursor uses a **fast model** to return structured allow/deny style results. See the official doc for **`$ARGUMENTS`** and optional **`model`**.

## Agent vs Tab events

**Agent** (Cmd+K / Agent chat) and **Tab** (inline completions) use **different** hook names.

**Agent (representative set from Cursor docs):**

| Direction | Examples |
|-----------|-----------|
| Session | `sessionStart`, `sessionEnd` |
| Tools | `preToolUse`, `postToolUse`, `postToolUseFailure` |
| Subagents | `subagentStart`, `subagentStop` |
| Shell | `beforeShellExecution`, `afterShellExecution` |
| MCP | `beforeMCPExecution`, `afterMCPExecution` |
| Files | `beforeReadFile`, `afterFileEdit` |
| Prompt / loop | `beforeSubmitPrompt`, `preCompact`, `stop`, `afterAgentResponse`, `afterAgentThought` |

**Tab:**

- `beforeTabFileRead`
- `afterTabFileEdit`

Use Tab hooks when policy for **autonomous inline edits** should differ from **explicit Agent** work.

## Examples (official doc patterns)

The Cursor doc ships full snippets for:

- **Audit logging** — append stdin JSON to a log in `afterFileEdit` / `beforeShellExecution` / etc.
- **Shell gating** — parse `.command` with `jq`, return `permission: deny|ask|allow` JSON from `beforeShellExecution`.
- **`stop` hook** — TypeScript/Bun example: persist metrics, optional telemetry HTTP, `followup_message` for automated retry messaging.
- **`beforeShellExecution`** — Python example: guard `kubectl`-style flows with structured parsing.

Use those as **copy-paste starting points**; keep project paths under **`.cursor/hooks/`**.

**Partner integrations** for security/governance/secrets are linked from the [Hooks doc § Partner integrations](https://cursor.com/docs/hooks#partner-integrations).

## Related in this repo

| File | Why |
|------|-----|
| `.steering/cursor/Agents.md` | Subagents (Task tool) and how they differ from hook-injected context. |
| `.steering/cursor/Rules.md` | Cursor **rules** (`.cursor/rules`) — complementary to hooks, not the same mechanism. |
| `.steering/agents/sync-agents.md` | Agent **markdown** mirroring from steering; unrelated to `hooks.json`, but often configured in the same product. |

## Resources

- [Hooks](https://cursor.com/docs/hooks) — full event list, JSON schemas, blocking semantics, examples.
- [Third-party hooks](https://cursor.com/docs/reference/third-party-hooks) — Claude Code and compatibility.
- [Cloud Agent](https://cursor.com/docs/cloud-agent) — where project hooks run in the cloud.
