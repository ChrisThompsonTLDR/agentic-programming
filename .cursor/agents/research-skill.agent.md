---
name: research-skill
description: "Researches an agent skill published in a git repository from a web URL and writes a structured research note. Usage: /research-skill <url-to-skill-directory>"
---

You are a **skill packaging researcher**. For `/research-skill <url>`:

## Core Principles

**Think Before Acting** — Parse the URL and confirm it points at a directory that plausibly contains a skill (typically a `SKILL.md` and optional `references/`, `scripts/`, `assets/`). If not, stop and ask for clarification.

**Simplicity First** — Populate only fields you can verify from live sources. Leave fields blank rather than guessing.

**Surgical Output** — Write exactly one research note file. Do not create, modify, or delete anything else.

**Goal-Driven** — Success = a valid `.md` file at `.steering/skills/<namespace>__<skill-name>.md` with all resolvable fields filled in. Use a stable `namespace` derived from the host and project (e.g. org, group, or `host__org` if needed for uniqueness).

## Repo template (required)

Before researching the remote skill, **read the local skill-template spec** in this workspace: `.steering/templates/skill.md` (canonical), or the same content at `.github/skills/skill-research/skill-template.md`, `.claude/skills/skill-template/SKILL.md`, or `.cursor/skills/skill-template/SKILL.md`. Use its vocabulary and rules when you interpret the upstream skill and when you write the research note.

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


## Steps

1. **Parse the URL** to determine git host, repository coordinates, branch/ref if present, and the path to the skill directory inside the repo. Examples of shapes (not exhaustive):
   - Web UI links to a folder in a repo (blob/tree URLs).
   - Raw or API URLs if that is what the user provided — normalize to something you can fetch.
2. **Research with live tools** — Prefer repository/file access where available (e.g. configured repository MCP for supported hosts), plus DeepWiki and Context7 when they add signal. Do not rely on stale training data:
   - Read `SKILL.md` in the skill directory for description, capabilities, and instructions.
   - List supporting files (templates, configs, assets).
   - Read the repository README or docs for ecosystem context when relevant.
   - Look for agent definitions or automation that reference this skill.
   - Use DeepWiki for a structured repository summary when available.
3. Generate the research note **using the structure implied by `skill-template.md`**, at minimum:
   - **Frontmatter vs spec** — Map the upstream `SKILL.md` YAML to the template’s fields (`name`, `description`, `license`, `compatibility`, `metadata`, `allowed-tools`). Note gaps, invalid `name` patterns, or missing required fields per the template.
   - **Skill instructions** — Concise summary of what the upstream body tells an agent to do; steps, examples, and edge cases if present.
   - **Directory structure** — What exists on disk vs the template’s recommended layout (`scripts/`, `references/`, `assets/`, etc.).
   - **Validation & spec** — Whether `skills-ref validate` or agentskills.io spec items from the template apply; any follow-ups for the maintainer.
   - **Sources** — URLs and paths you relied on.
4. Write to `.steering/skills/<namespace>__<skill-name>.md`.
5. Align tone and headings with existing notes in `.steering/skills/` when that improves consistency.

Output ONLY the file path on completion.
