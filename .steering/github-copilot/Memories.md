---
title: Copilot Memory
url: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/copilot-memory
feature_status: Public preview
who_can_use:
  - Enterprises/orgs with Copilot Enterprise/Business
  - Individuals with Copilot Pro/Pro+
tags: [github, copilot, memory, agents, ai]
related_features: [Copilot cloud agent, Copilot code review, Copilot CLI]
---

# Copilot Memory

Copilot Memory allows GitHub Copilot to learn about your codebase, improving effectiveness for **Copilot cloud agent**, **Copilot code review**, and **Copilot CLI** in repositories.

> **Note**: Currently in [public preview](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/copilot-memory) and subject to change.

![Copilot Memory List Screenshot](https://docs.github.com/assets/cb-332961/images/help/copilot/copilot-memory-list.png)

## Key Benefits
- Stores codebase insights (memories) for better agentic decisions
- Automatic validation: Only uses memories if source code still exists
- Auto-deletion: Memories expire after **28 days** to prevent staleness
- Repo owners can view/delete inappropriate memories

## Enabling Copilot Memory

### Enterprise Level
Enterprise owners set policy:
1. Enterprise Settings → **AI controls** → **Copilot** → **Copilot Memory**
2. Options: **Let organizations decide** | **Enabled everywhere** | **Disabled everywhere**

### Organization Level
Org owners enable for members with Copilot license:
1. Org Settings → **Copilot** → **Policies** → **Copilot Memory** → **Enabled**

### Individual Users (Pro/Pro+)
Enabled by default:
1. Profile → **Copilot settings** → **Copilot Memory** → **Enabled/Disabled**

> **Note**: Most restrictive policy applies if user in multiple orgs.

## Viewing Memories (Repo Owners)
1. Repo → **Settings** → **Copilot** → **Memory**
2. Lists memories chronologically (newest first)

![Repo Settings Screenshot](https://docs.github.com/assets/cb-28260/images/help/repository/repo-actions-settings.png)

## Deleting Memories
- Click trash icon per memory
- Or select multiple → **Delete**

Copilot re-validates before use.

## Resources
- [Official Docs](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/copilot-memory)
- [About Copilot Memory](https://docs.github.com/en/copilot/concepts/agents/copilot-memory)
- [Copilot Plans](https://github.com/features/copilot/plans)

## Related Notes
[[Github Copilot]]
