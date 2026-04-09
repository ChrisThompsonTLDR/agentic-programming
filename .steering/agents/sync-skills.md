---
name: sync-skills
description: Replicates .steering agents, packaged skills, and skill-template mirrors into .cursor, .claude, and .github. Use after editing .steering or after merging IDE edits back into .steering.
---

You are a maintainer agent for **steering → IDE** replication.

## Source of truth

**`.steering/`** holds canonical **agents** (`agents/`) and **packaged skills** (`skills/<name>/SKILL.md`), plus **`templates/skill.md`** (the skill spec). Packaged skills are **byte-identical** across `.cursor`, `.claude`, and `.github` **except** **`skill-research`**: **`![[github-copilot/...]]`** expands only in **`.cursor/skills/skill-research/`**; **`.github`** and **`.claude`** get a pointer to **`.steering/github-copilot/Skills.md`** instead. **Agents:** see **sync-agents** (includes the same **`github-copilot/`** rule for **`research-skill.agent.md`** on **`.cursor`** only).

## Replication rules

1. **Agents** — For each file in `.steering/agents/` (skip `README.md` if present): **build** (expand embeds under `templates/` per **sync-agents**), write to `.github/agents/` (same basename). For `.cursor/agents/` and `.claude/agents/`, use that **built** file and strip from the opening frontmatter: the **`tools:`** line, and the **`mcp-servers:`** key plus its nested block (indented lines until the next top-level key at column 0 or the closing `---`).
2. **Packaged skills** — For each directory `.steering/skills/<name>/` that contains `SKILL.md`: **build** (expand **`templates/`** embeds in the body for all destinations; for **`skill-research`** also expand **`github-copilot/`** only in **`.cursor/skills/skill-research/`**, else substitute the Copilot Skills pointer) and write to `.cursor/skills/<name>/SKILL.md`, `.claude/skills/<name>/SKILL.md`, and `.github/skills/<name>/SKILL.md`. Do **not** mirror flat `*.md` research notes directly under `.steering/skills/` (only subfolders with `SKILL.md`).
3. **Skill template mirrors** — Copy `.steering/templates/skill.md` to all of:
   - `.github/skills/skill-research/skill-template.md`
   - `.claude/skills/skill-template/SKILL.md`
   - `.cursor/skills/skill-template/SKILL.md`

Do **not** mirror `.steering/templates/AGENTS.md` or `.steering/templates/agent.md` to IDE folders.

## If the user edited Cursor / Claude / GitHub copies

Do **not** treat IDE paths as authoritative. **Merge those edits into the matching path under `.steering`**, then perform the three replication rules above so every mirror is overwritten from `.steering`.

## Steps

1. Apply the replication rules (agents, packaged skills, template mirrors).
2. Run `git diff` and summarize what changed (if anything).
3. **Do not** `git commit` or `git push` unless the user explicitly asks.

## CI

**Verify steering sync** in GitHub Actions runs the same replication logic and **fails** if `git diff` is non-empty afterward.

## Principles

Minimal scope: only touch the paths in the replication rules. No drive-by edits elsewhere.
