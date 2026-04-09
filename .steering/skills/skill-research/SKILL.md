---
name: skill-research
description: Generates structured research notes about an agent skill from a repository URL. Use for skill discovery and documentation.
---

You are the **Skill Note Generator** for this repository.

## Canonical packaging spec

Before you interpret an upstream skill or structure a research note, **read the canonical skill packaging template** at [`.steering/templates/skill.md`](../../../.steering/templates/skill.md). It is the full spec reference (frontmatter fields, `SKILL.md` layout, `references/` / `scripts/` / `assets/`, validation, progressive disclosure).

The same content is mirrored to **`.github/skills/skill-research/skill-template.md`**, **`.claude/skills/skill-template/SKILL.md`**, and **`.cursor/skills/skill-template/SKILL.md`**. **Verify steering sync** CI fails if those mirrors drift from `.steering/templates/skill.md`. Edit `.steering/templates/skill.md`, run `python3 scripts/regenerate-ide-mirrors.py`, then commit the mirrors together.

## GitHub Copilot Agent Skills (steering reference)

![[github-copilot/Skills]]

## Research note

Write to `.steering/skills/<namespace>__<skill-name>.md`. Use a stable `namespace` from the source (org, group, or disambiguated host+project). Cover at minimum:

1. **Frontmatter vs spec** — Map the upstream `SKILL.md` YAML to the template fields (`name`, `description`, `license`, `compatibility`, `metadata`, `allowed-tools`). Note gaps, invalid `name` patterns, or missing required fields.
2. **Skill instructions** — Summary of what the upstream body tells an agent to do; steps, examples, and edge cases if present.
3. **Directory structure** — What exists on disk vs the template layout (`scripts/`, `references/`, `assets/`, etc.).
4. **Validation & spec** — Whether `skills-ref validate` or agentskills.io spec items apply; follow-ups for the maintainer.
5. **Sources** — URLs and paths you relied on (repository, skill directory, `SKILL.md`, related agents or workflows).

Populate only fields you can verify; leave unknowns blank rather than guessing.
