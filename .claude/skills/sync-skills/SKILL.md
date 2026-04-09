---
name: sync-skills
description: Replicates .steering agents, packaged skills, and skill-template mirrors into .cursor, .claude, and .github. Does not commit. Use after editing .steering or after merging IDE copies back into .steering.
license: MIT
compatibility: Repo with .steering layout; use editor or file copy as needed.
metadata:
  author: agentic-programming
  version: "1.0"
---

# Sync skills (steering → IDEs)

## When to use

- Anything under `.steering/agents/`, `.steering/skills/*/SKILL.md`, or `.steering/templates/skill.md` changed.
- The user edited `.cursor/`, `.claude/`, or `.github/` copies — merge into `.steering` first, then replicate out.
- Matching **Verify steering sync** CI locally.

## Replication rules

1. **Agents** — Build each `.steering/agents/*.md` per **sync-agents** (templates + special **`github-copilot/`** handling for **`research-skill.agent.md`** on **`.cursor`** only), write to `.github/agents/`, then strip Copilot **`tools:`** / **`mcp-servers:`** for `.cursor/agents/` and `.claude/agents/`.
2. **Packaged skills** — For each `.steering/skills/<name>/SKILL.md`: build (templates embeds; **`skill-research`**: **`github-copilot/`** embed only under **`.cursor/skills/skill-research/`**) and write to `.cursor/skills/<name>/SKILL.md`, `.claude/skills/<name>/SKILL.md`, `.github/skills/<name>/SKILL.md`. Flat `*.md` under `.steering/skills/` (research notes) are **not** mirrored.
3. **Skill template mirrors** — Copy `.steering/templates/skill.md` to:
   - `.github/skills/skill-research/skill-template.md`
   - `.claude/skills/skill-template/SKILL.md`
   - `.cursor/skills/skill-template/SKILL.md`

## Steps

1. Apply the replication rules above (or run `python3 scripts/regenerate-ide-mirrors.py` from the repo root to match CI exactly).
2. Run `git diff`. If empty, mirrors already matched.
3. **Do not** `git add` / `git commit` / `git push` unless the user explicitly asks.

## CI

**Verify steering sync** (`.github/workflows/verify-steering-sync.yml`) runs `python3 scripts/regenerate-ide-mirrors.py` and fails on `git diff`.

## Upstream skills

If skills were refreshed from an external catalog (see `.steering/skills/SOURCES.md`), run `python3 scripts/sync-boost-ai-skills.py` first, then `python3 scripts/regenerate-ide-mirrors.py`.
