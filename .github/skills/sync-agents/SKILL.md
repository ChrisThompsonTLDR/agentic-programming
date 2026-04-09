---
name: sync-agents
description: Builds .steering/agents (Obsidian ![[ embeds expanded), writes .github/agents, then .cursor/.claude with Copilot YAML stripped. Does not commit.
license: MIT
compatibility: Same embed rules as verify-steering-sync.yml (Python or manual).
metadata:
  author: agentic-programming
  version: "1.0"
---

# Sync agents (steering → IDEs)

## When to use

- Anything under `.steering/agents/` changed.
- Merge IDE edits back into `.steering/agents/` first, then replicate.

## Replication rules

1. **Build** — In each agent file’s **body** (after opening YAML), expand **`<!-- missing: .steering/templates/....md -->
`** by default. For **`research-skill.agent.md`**, also expand **`![[github-copilot/...]]`** only in the **`.cursor/agents/`** output; **`.github`** / **`.claude`** replace those embeds with a pointer to **`.steering/github-copilot/Skills.md`**. With `#Heading`, inline the `## Heading` section only. Leave other `![[...]]` as-is.

2. **`.github/agents/`** — Write the **built** markdown (same basename).

3. **`.cursor/agents/`** and **`.claude/agents/`** — Built file, then strip **`tools:`** and **`mcp-servers:`** from the opening frontmatter.

4. Do **not** touch skills or skill-template paths.

## Steps

1. Apply the rules above (match **Verify steering sync** agent step).
2. Run `git diff`.
3. **Do not** commit unless the user asks.

## CI

**Verify steering sync** implements the same build + strip logic.
