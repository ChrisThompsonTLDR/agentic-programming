---
title: Cursor Agent Skills
url: https://cursor.com/docs/skills
tags: [cursor, skills, SKILL.md, agentskills, progressive-disclosure]
related:
  - "[[cursor/Rules]]"
  - "[[cursor/Agents]]"
  - "[[cursor/Plugins]]"
  - "[[github-copilot/Skills]]"
---

# Cursor Agent Skills

**Official reference:** [Agent Skills | Cursor Docs](https://cursor.com/docs/skills) · **Open standard:** [agentskills.io](https://agentskills.io)

**Skills** are portable, file-based packages that teach **Agent (Chat)** how to do a **focused task** (workflows, conventions, checklists). They can ship **scripts**, **references**, and **assets** the agent uses via tools. Cursor **discovers** them at startup and usually includes them when context suggests relevance; users can also invoke **`/skill-name`** manually.

## Skills vs rules vs subagents

| Mechanism | Typical use |
|-----------|-------------|
| **Rules** | Always-on or glob-scoped **policy** and project norms (see **`.steering/cursor/Rules.md`**). |
| **Skills** | **Procedure packs**—steps, examples, optional scripts—loaded **progressively** when relevant. |
| **Subagents** | **Separate context windows** for heavy exploration, shell noise, or parallel work (see **`.steering/cursor/Agents.md`**). |

Cursor’s subagents doc includes a **when to use subagents vs skills** table; prefer skills for **single-shot, repeatable** playbooks when you do **not** need isolation.

## Where Cursor loads skills from

| Location | Scope |
|----------|--------|
| **`.cursor/skills/`** | Project |
| **`.agents/skills/`** | Project (alternate layout in docs) |
| **`~/.cursor/skills/`** | User (global) |

**Compatibility paths** (also scanned): **`.claude/skills/`**, **`.codex/skills/`**, and the matching **`~/.claude/`** / **`~/.codex/`** trees.

Each skill is a **directory** whose name matches the skill **`name`** in frontmatter, containing **`SKILL.md`** at its root.

## Directory layout

```text
my-skill/
├── SKILL.md
├── scripts/       # optional
├── references/    # optional
└── assets/        # optional
```

Keep **`SKILL.md`** lean; put long prose in **`references/`** so the agent can load it **on demand**.

## `SKILL.md` format

YAML frontmatter + markdown body. Minimal shape (from Cursor docs):

```markdown
---
name: my-skill
description: What it does and when to use it (helps the model choose it).
---

# My Skill
…
```

### Frontmatter fields (Cursor)

| Field | Required | Notes |
|--------|----------|--------|
| `name` | Yes | Lowercase letters, numbers, hyphens; **must match the parent folder name**. |
| `description` | Yes | Used for **relevance** and discovery; include trigger keywords. |
| `license` | No | |
| `compatibility` | No | Environment / tooling assumptions. |
| `metadata` | No | Arbitrary key-value map. |
| `disable-model-invocation` | No | If **`true`**, only applies when the user runs **`/skill-name`** (no automatic inclusion). |

**Repo spec:** This project’s **`allowed-tools`** and stricter field notes live in **`.steering/templates/skill.md`** (mirrored into **`.cursor/skills/skill-template/SKILL.md`** for authoring).

## Discovery and UI

- Agent sees available skills and **decides** when to apply them (unless `disable-model-invocation: true`).
- **Manual:** type **`/`** in Agent chat and pick the skill.
- **Settings:** **Cursor Settings → Rules** → skills appear under **Agent Decides** (per Cursor docs).

## GitHub install

Cursor documents importing from GitHub via **Settings → Rules → Add Rule → Remote Rule (GitHub)** with a repository URL (same flow as remote rules). See the Skills doc for the exact steps in your Cursor version.

## Migrating rules/commands → skills

Built-in **`/migrate-to-skills`** (Cursor **2.4+**) converts eligible **dynamic rules** and **slash commands** into **`.cursor/skills/`** folders. Rules with **`alwaysApply: true`** or **`globs`** stay as rules; **user rules** are not migrated. Details in [Agent Skills](https://cursor.com/docs/skills) § migrating.

## How this repo models skills

| Layer | Role |
|--------|------|
| **Canonical source** | **`.steering/skills/<name>/SKILL.md`** — edit packaged skills here first. |
| **Mirrors** | **Byte-identical** copies under **`.cursor/skills/<name>/`**, **`.claude/skills/<name>/`**, **`.github/skills/<name>/`** (see **`.steering/agents/sync-skills.md`** and **`.github/workflows/verify-steering-sync.yml`**). |
| **Spec / template** | **`.steering/templates/skill.md`** → also copied to **`skill-template`** paths and **`.github/skills/skill-research/skill-template.md`**. |
| **Research notes** | Flat **`.steering/skills/*.md`** (e.g. `<owner>__<skill>.md`) are **not** mirrored as packaged skills—only folders containing **`SKILL.md`**. |

**Packaged skills in steering today** (examples): `sync-agents`, `sync-skills`, `agentic-programming`, `skill-research`, `laravel-research`.

**Plugins:** Skills can ship inside a Cursor **plugin**; see **`.steering/cursor/Plugins.md`**.

## Related in this repo

| File | Why |
|------|-----|
| `.steering/templates/skill.md` | Field-level spec and layout for new **`SKILL.md`** files. |
| `.steering/agents/sync-skills.md` | Maintainer agent: replication rules for skills + agents + template. |
| `.steering/skills/sync-skills/SKILL.md` | Human-oriented steps to run sync locally. |
| `.steering/github-copilot/Skills.md` | **GitHub Copilot** cloud skills vs **Cursor** project skills. |

## Resources

- [Agent Skills (Cursor)](https://cursor.com/docs/skills) — directories, frontmatter, scripts, migration.
- [agentskills.io](https://agentskills.io) — open specification.
- [Rules](https://cursor.com/docs/rules) — how rules and skills appear together in Settings.
- [Subagents](https://cursor.com/docs/subagents) — delegation vs skills.
