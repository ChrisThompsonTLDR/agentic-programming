---
title: Copilot Agent Skills
url: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/create-skills
feature_status: Public Preview
who_can_use: Copilot Pro+, Business, Enterprise (cloud agent, CLI, VS Code agent mode)
tags:
  - github-copilot
  - agents
  - skills
  - customization
related:
 - [["GitHub Copilot/Agents"]]
 - [["GitHub Copilot/Memories"]]
---

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
