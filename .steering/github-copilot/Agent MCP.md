---
title: Extending Copilot Cloud Agent with MCP
url: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/extend-cloud-agent-with-mcp
status: Public Preview
tags: [copilot, mcp, agents, cloud-agent]
related: [[github-copilot/Agents]], [[github-copilot/Skills]]
---

# Extending GitHub Copilot Cloud Agent with Model Context Protocol (MCP)

Repository admins can configure MCP servers via JSON in repo settings. Org/enterprise admins can use YAML in custom agents.

## Prerequisites
- Understand [MCP and Cloud Agent](https://docs.github.com/en/copilot/concepts/agents/cloud-agent/mcp-and-cloud-agent)

## Adding MCP Config to Repository
1. Repo → **Settings** → **Copilot** → **MCP**
2. Paste JSON config in **MCP Servers** field

![Repo Settings Screenshot](https://docs.github.com/assets/cb-28260/images/help/repository/repo-actions-settings.png)

## JSON Configuration Format
```json
{
  "mcpServers": {
    "sentry": {
      "command": "npx",
      "args": ["-y", "@sentry/mcp-server-sentry"],
      "env": {
        "SENTRY_DSN": "$SENTRY_DSN"
      }
    },
    "notion": {
      "type": "sse",
      "url": "https://your-notion-mcp-server.com/sse",
      "headers": {
        "Authorization": "Bearer $NOTION_TOKEN"
      },
      "tools": ["list_databases", "read_page"]
    }
  }
}
```

### Server Types
| Type | Config Keys | Example |
|------|-------------|---------|
| Local (command) | `command`, `args[]`, `env`, `cwd`, `tools[]` | `npx @sentry/mcp-server-sentry` |
| Remote SSE | `type: "sse"`, `url`, `headers`, `tools[]` | Cloudflare SSE endpoint |
| Remote Streamable HTTP | `type: "streamable-http"`, `url`, `headers`, `tools[]` | OAuth not supported |

## Variable Substitution
| Syntax | Example |
|--------|---------|
| `$VAR` | `$COPILOT_MCP_API_KEY` |
| `${VAR}` | `${COPILOT_MCP_API_KEY}` |
| `${VAR:-default}` | `${COPILOT_MCP_API_KEY:-fallback}` |

## Environment Secrets
- Repo: **Settings** → **Secrets and variables** → **Actions** → New secret (`COPILOT_MCP_*`)
- Auto-injected for local MCP servers

## Examples
### Sentry
```json
{
  "mcpServers": {
    "sentry": {
      "command": "npx",
      "args": ["-y", "@sentry/mcp-server-sentry"],
      "env": { "SENTRY_DSN": "$SENTRY_DSN" },
      "tools": ["*"]
    }
  }
}
```

### Notion
```json
{
  "mcpServers": {
    "notion": {
      "command": "npx",
      "args": ["-y", "notion-mcp-server"],
      "env": { "NOTION_API_KEY": "$NOTION_API_KEY" }
    }
  }
}
```

### Azure (via workflow OIDC)
Update `copilot-setup-steps.yml` for Azure login.

### Cloudflare
```json
{
  "mcpServers": {
    "cloudflare": {
      "type": "sse",
      "url": "https://docs.mcp.cloudflare.com/sse",
      "tools": ["*"]
    }
  }
}
```

### Azure DevOps / Atlassian
Similar command/env setups; see docs for auth (OIDC/API tokens).

## Reusing VS Code MCP Config
- Copy from `.vscode/mcp.json` or `settings.json`
- Add `tools: ["*"]` or specific tools
- Adapt env vars to repo secrets

## Validation & Warnings
- **Autonomous Tools**: Copilot may call tools without explicit instruction
- **Read-Only Recommended**: Avoid destructive actions
- **No OAuth Remotes**: Only basic auth/headers/tokens
- **GitHub MCP**: Repo owners can customize via `.github/mcp.json`

## Resources
- [Docs](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/extend-cloud-agent-with-mcp)
- Related: [[github-copilot/Agents]], [[github-copilot/Skills]], [[github-copilot/Memories]]