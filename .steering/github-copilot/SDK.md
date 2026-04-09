---
title: Copilot SDK Skill
github_url: https://github.com/microsoft/skills/tree/main/.github/skills/copilot-sdk
repo_url: https://github.com/microsoft/skills
repo_stars: 2k
repo_forks: 218
last_commit: 2026-02-19
author: thegovind & Copilot
tags: [copilot, skills, sdk, microsoft, mcp, hooks, deployment]
related:
 - [[GitHub Copilot/Skills]]
 - [[GitHub Copilot/Agents]]
 - [[GitHub Copilot/Agent MCP]]
---

# Copilot SDK Skill

From the official [Microsoft Skills repo](https://github.com/microsoft/skills) (2k⭐, 218 forks)—a curated collection of GitHub Copilot agent skills.

This skill provides **comprehensive guidance on the Copilot SDK**, covering API usage, hooks, authentication, MCP integration, deployment patterns, and more. Latest expansion (Feb 18, 2026) grew from ~510 to ~900 lines for full coverage.

## Key Features (from SKILL.md commits)
- **Architecture**: Transport modes (stdio/TCP).
- **Hooks**: All 6 lifecycle hooks (pre/post tool use, user prompt, session start/end, error handling) with multi-language examples.
- **BYOK (Bring Your Own Keys)**: Provider configs (OpenAI, Azure OpenAI, Anthropic, Ollama). Reference table + Azure Managed Identity pattern.
- **Authentication**: Priority order, OAuth GitHub App, token types, disable auto-login.
- **Session Persistence**: Resume options, session ID best practices, persisted data, infinite sessions.
- **MCP Server Integration**: Local/HTTP configs (all fields), debugging (MCP Inspector).
- **Deployment Patterns**:
  | Pattern | Description |
  |---------|-------------|
  | Local CLI | `copilot-sdk run` |
  | External Server | TCP/HTTP endpoints |
  | Bundled CLI | Embed in apps |
  | Docker Compose | Multi-container |
  | Session Isolation | Prod checklist |
- **Permissions/Input Handlers**: Deny-by-default model.
- **SDK vs CLI Comparison**: Feature table + workarounds.
- **Debugging**: Common issues table, connection states.

## Directory Structure
```
.github/skills/copilot-sdk/
├── SKILL.md          # Main instructions (~900 lines)
└── references/       # Supporting docs/examples
    └── (various files for tests/acceptance criteria)
```

## Usage
1. **Add to your repo**: Copy `.github/skills/copilot-sdk/` to `.github/skills/copilot-sdk/` (auto-discovered).
2. **Invoke**: Copilot loads when relevant (e.g., "build Copilot SDK app", "add MCP to agent").
3. **Test Coverage**: 11/11 scenarios pass (98.2% avg score, Feb 2026).

## Resources
- [SKILL.md (raw)](https://github.com/microsoft/skills/blob/main/.github/skills/copilot-sdk/SKILL.md)
- [Repo README](https://github.com/microsoft/skills)
- [Latest Commit](https://github.com/microsoft/skills/commit/e13c7df45bc86c49ccbcb1376a01e343be777651)

## Related Notes
- [[GitHub Copilot/Skills]]: General skills guide.
- [[GitHub Copilot/Agent MCP]]: MCP configs for SDK.
- [[Workflows/Agent Sync]]: Sync skills across agents (regenrek/agent-skills).

---
*Last updated: 2026-04-08*
