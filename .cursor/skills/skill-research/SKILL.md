---
name: skill-research
description: Generates structured research notes about an agent skill from a repository URL. Use for skill discovery and documentation.
---

You are the **Skill Note Generator** for this repository.

## Canonical packaging spec

Before you interpret an upstream skill or structure a research note, **read the canonical skill packaging template** at [`.steering/templates/skill.md`](../../../.steering/templates/skill.md). It is the full spec reference (frontmatter fields, `SKILL.md` layout, `references/` / `scripts/` / `assets/`, validation, progressive disclosure).

The same content is mirrored to **`.github/skills/skill-research/skill-template.md`**, **`.claude/skills/skill-template/SKILL.md`**, and **`.cursor/skills/skill-template/SKILL.md`**. **Verify steering sync** CI fails if those mirrors drift from `.steering/templates/skill.md`. Edit `.steering/templates/skill.md`, run `python3 scripts/regenerate-ide-mirrors.py`, then commit the mirrors together.

## GitHub Copilot Agent Skills (steering reference)

# Copilot Agent Skills

Agent skills modify Copilot's behavior for specific tasks via folders with `SKILL.md` (YAML frontmatter + instructions) + optional scripts/resources.

**Works with**: Copilot cloud agent, GitHub Copilot CLI, VS Code agent mode.

## Purpose vs Custom Instructions
- **Skills**: Detailed, task-specific (e.g., debugging workflows). Loaded when relevant via description matching.
- **Custom Instructions**: Repo-wide general rules (coding standards).

## Creating/Adding Skills

1. Create folder: 
   - **Project**: `.github/skills/{skill-name}/` (repo-specific)
   - **Personal**: `~/.copilot/skills/{skill-name}/` (global)

2. Add `SKILL.md` with YAML frontmatter:
   ```yaml
   ---
   name: github-actions-failure-debugging
   description: Guide for debugging failing GitHub Actions workflows. Use this when asked to debug failing GitHub Actions workflows.
   ---
   
   You are a testing specialist focused on improving code quality...
   ```

3. **Optional**: Add scripts/resources in folder—Copilot auto-discovers and references them.

### Example: GitHub Actions Debugging
```text
.github/skills/github-actions-failure-debugging/
├── SKILL.md
└── debug-workflow.sh  # Script Copilot can run
```

### Running Scripts
- Copilot discovers files in skill dir.
- Reference in instructions: "Run `./debug-workflow.sh` to analyze logs."
- **Security**: Scripts must be explicitly allowed; Copilot prompts before execution.

## How Copilot Uses Skills
1. Matches prompt to skill `description`.
2. Injects `SKILL.md` + dir files into context.
3. Follows instructions, runs allowed scripts/tools.

## Example Skills
### GitHub Actions Failure Debugging
```yaml
---
name: github-actions-failure-debugging
description: Guide for debugging failing GitHub Actions workflows...
---
You are a GitHub Actions debugging expert...
1. Read workflow YAML...
2. Check logs...
```

### SVG to PNG Converter
Include `convert-svg.sh` script; instructions reference it.

## Resources
- [Official Docs](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/create-skills)
- [Awesome Copilot Agents](https://github.com/github/awesome-copilot/tree/main/agents)

## Related Notes
[[GitHub Copilot/Agents]] | [[GitHub Copilot/Memories]] | [[Laravel Packages]]


## Research note

Write to `.steering/skills/<namespace>__<skill-name>.md`. Use a stable `namespace` from the source (org, group, or disambiguated host+project). Cover at minimum:

1. **Frontmatter vs spec** — Map the upstream `SKILL.md` YAML to the template fields (`name`, `description`, `license`, `compatibility`, `metadata`, `allowed-tools`). Note gaps, invalid `name` patterns, or missing required fields.
2. **Skill instructions** — Summary of what the upstream body tells an agent to do; steps, examples, and edge cases if present.
3. **Directory structure** — What exists on disk vs the template layout (`scripts/`, `references/`, `assets/`, etc.).
4. **Validation & spec** — Whether `skills-ref validate` or agentskills.io spec items apply; follow-ups for the maintainer.
5. **Sources** — URLs and paths you relied on (repository, skill directory, `SKILL.md`, related agents or workflows).

Populate only fields you can verify; leave unknowns blank rather than guessing.
