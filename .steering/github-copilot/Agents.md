---
title: Copilot Custom Agents
url: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/create-custom-agents
feature_status: Public Preview
who_can_use: Copilot Pro/Pro+/Business/Enterprise
tags: [github-copilot, agents, custom-agents, cloud-agent, mcp]
related: [[Github Copilot/Memories]]
---

# Copilot Custom Agents

![Copilot Agents](https://docs.github.com/assets/cb/copilot/agents/custom-agent.png)

**Tailor Copilot's expertise** for specific tasks via `.agent.md` profiles in `.github/agents/` (repo/workspace) or root `agents/` (org/enterprise).

## Who Can Use
- **Plans**: Copilot Pro/Pro+, Business, Enterprise
- **Availability**: All GitHub repos (except managed users/disabled)
- **IDEs**: VS Code, JetBrains, Eclipse, Xcode (preview)

## Creating Agent Profiles

### On GitHub.com
1. [github.com/copilot/agents](https://github.com/copilot/agents) → Select repo/branch
2. Create `my-agent.agent.md` in `.github/agents/`
3. Org/Ent: Move to root `agents/`
4. Edit YAML + prompt → Commit

### In IDEs
- **VS Code/JetBrains/Eclipse/Xcode**: Chat dropdown → Configure/Create → `.agent.md` in `.github/agents` (workspace) or user profile

## Configuration (YAML Frontmatter + Markdown Prompt)
```yaml
---
name: test-specialist  # Defaults to filename
description: >  # Required
  Focuses on test coverage...
tools: ["read", "edit", "search"]  # Or omit for all
mcp-servers: [...]  # Agent-specific MCP
model: gpt-4o  # IDEs only
target: vscode  # vscode/github-copilot
---
# Prompt (max 30k chars): Instructions, expertise, behavior
You are a testing specialist...
```

- **Tools**: Built-in (read/edit/search) + MCP servers/aliases
- **Docs**: [Custom Agents Config](https://docs.github.com/en/copilot/reference/custom-agents-configuration)

## Example Profiles

### Testing Specialist
```yaml
---
name: test-specialist
description: Focuses on test coverage...
---
# Analyzes gaps, writes unit/integration/E2E tests
# Never modifies prod code
```

### Implementation Planner
```yaml
---
name: implementation-planner
description: Creates detailed specs...
tools: ["read", "search", "edit"]
---
# Breaks down reqs, docs APIs/models, risks
```

More: [Customization Library](https://docs.github.com/en/copilot/tutorials/customization-library/custom-agents), [awesome-copilot/agents](https://github.com/github/awesome-copilot/tree/main/agents)

## Using Custom Agents
- **GitHub**: Agents tab/prompt dropdown; Issue assignment; PRs note agent used
- **Chat/CLI**: `@agent` or dropdown/slash `/agent`
- **IDEs**: Chat agent dropdown

## Next Steps
- [Your First Custom Agent Tutorial](https://docs.github.com/en/copilot/tutorials/customization-library/custom-agents/your-first-custom-agent)
- [Create PR with Agent](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/create-a-pr)

## Resources
- [GitHub Docs](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/create-custom-agents)
- [About Custom Agents](https://docs.github.com/en/copilot/concepts/agents/cloud-agent/about-custom-agents)
