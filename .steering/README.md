# `.steering` — source of truth

Canonical **agents** and **packaged skills** live here. **Packaged skills** and **skill-template** mirrors are usually identical under `.cursor`, `.claude`, and `.github`; **exception:** **`skill-research`** expands **`![[github-copilot/...]]`** only in **`.cursor/skills/skill-research/`** (other mirrors get a pointer to **`.steering/github-copilot/Skills.md`**). **Agents** may use **`![[templates/...]]`**; **`research-skill.agent.md`** uses the same **`github-copilot/`** rule for **`.cursor/agents/`** only. **Mirrors** are **built** (embeds expanded per destination), then **`.cursor/agents/`** and **`.claude/agents/`** drop Copilot-only **`tools:`** / **`mcp-servers:`**. CI also asserts Cursor/Claude agent mirrors never contain those keys.

## Layout

| Path | Purpose |
|------|---------|
| `agents/` | Agent definitions (`![[templates/...]]`; **`research-skill.agent.md`:** **`![[github-copilot/...]]`** expanded on **`.cursor`** only). **`.github/agents/`** = built; **`.cursor`** / **`.claude`** = built (per rules) + strip **`tools:`** / **`mcp-servers:`** (skip `README.md` if you add one). |
| `skills/<name>/SKILL.md` | Packaged skills — **built** to each IDE (same as agents for embeds; **`skill-research`** Copilot note inlined only under **`.cursor/skills/`**). |
| `skills/<owner>__<skill>.md` | Skill research notes only — not mirrored. |
| `mcps/<owner>__<name>.md` | MCP server research notes (`research-mcp` agent) — not mirrored. |
| `templates/skill.md` | Skill spec; also copy to `skill-template` paths below. |
| `templates/AGENTS.md` | Starter for repo-root **`AGENTS.md`** (skills + MCP); not mirrored — see **sync-agents**. |
| `templates/agent.md` | **Core Principles** only (embedded by some agents); not mirrored. |

**Template mirrors** (from `templates/skill.md`):

- `.github/skills/skill-research/skill-template.md`
- `.claude/skills/skill-template/SKILL.md`
- `.cursor/skills/skill-template/SKILL.md`

Packaged skill **`sync-skills`** covers full replication; **`sync-agents`** covers `.steering/agents/` only.

## Workflow

1. Edit under `.steering/` (or merge IDE edits **into** `.steering` first).
2. Replicate to the three IDE roots: same files, same paths relative to each root’s `agents/` and `skills/` layout, plus the three template paths above.
3. Commit `.steering/**` and every updated mirror in one change when possible.

CI (**Verify steering sync**) repeats those copies in the runner and fails if `git diff` is non-empty.
