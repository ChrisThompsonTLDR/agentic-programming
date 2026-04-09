---
title: Copilot Settings - MCP Configuration
url: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/extend-cloud-agent-with-mcp
feature_status: Public Preview
who_can_use: Repository administrators, Org/Enterprise owners
tags: [copilot, mcp, settings, cloud-agent, agents]
related: 
  - [[github-copilot/Agents]]
  - [[github-copilot/Skills]]
  - [[github-copilot/Agent MCP]]
---

# Copilot Settings: Extending Cloud Agent with MCP

Research note on configuring **Model Context Protocol (MCP)** servers in GitHub Copilot settings to extend cloud agent capabilities.

## Overview
Repository admins configure MCP servers via JSON in repo **Settings > Copilot > MCP Servers**.

- **Purpose**: Give Copilot access to external tools/services (Sentry, Notion, Azure, etc.) via MCP.
- **Security**: Copilot decides tool use autonomously—use read-only where possible.
- **Types**: Local (command/args), Remote SSE/Streamable HTTP.

![Repo Settings Navigation](https://docs.github.com/assets/cb-28260/images/help/repository/repo-actions-settings.png)

## Prerequisites
- Understand [MCP and Cloud Agent](https://docs.github.com/en/copilot/concepts/agents/cloud-agent/mcp-and-cloud-agent).

## Repo Configuration
Navigate: Repo **Settings > Copilot > MCP Servers**.

JSON format:
```json
{
  "mcpServers": {
    "sentry": {
      "type": "local",
      "command": "npx",
      "args": ["-y", "@sentry/mcp-server@sentry-mcp-server"],
      "env": {
        "SENTRY_MCP_DSN": "${SENTRY_MCP_DSN}"
      },
      "tools": ["search_issues"]
    },
    "notion": {
      "type": "sse",
      "url": "https://your-notion-mcp-server.com/sse",
      "headers": {
        "Authorization": "Bearer ${NOTION_TOKEN}"
      },
      "tools": ["listPages", "readPage"]
    }
  }
}
```

### Variable Substitution
| Syntax | Example |
|--------|---------|
| `$VAR` | `$COPILOT_MCP_API_KEY` |
| `${VAR}` | `${COPILOT_MCP_API_KEY}` |
| `${VAR:-default}` | `${COPILOT_MCP_API_KEY:-fallback}` |

**Environment Variables**: Set in Repo **Settings > Secrets and variables > Actions**.

## Server Examples
- **[Sentry](https://github.com/getsentry/sentry-mcp)**: Exceptions access.
- **[Notion](https://github.com/makenotion/notion-mcp-server)**: Notes/docs.
- **[Azure](https://github.com/microsoft/mcp)**: Resources/files.
- **[Cloudflare](https://github.com/cloudflare/mcp-server-cloudflare)**: Services/docs.
- **[Azure DevOps](https://github.com/microsoft/azure-devops-mcp)**: Work items/pipelines (needs OIDC).
- **[Atlassian](https://github.com/atlassian/atlassian-mcp-server)**: Jira/Confluence (API token).

Full JSON examples in doc.

## VS Code Reuse
Adapt `.vscode/mcp.json`:
- Add `"tools": ["*"]` or specific.
- Wrap in `"mcpServers": { ... }`.

## Environment Secrets
- Repo: **Settings > Secrets > Actions** (e.g., `AZURE_CLIENT_ID`).
- Org/Enterprise: Centralized management.

## Validation & Warnings
- **Test**: Copilot validates before use (code must exist).
- **Read-only recommended**: Avoid destructive tools.
- **No OAuth remotes**: Use SSE/HTTP with tokens.
- **GitHub MCP**: Customize via custom agents YAML.

## Resources
- [Full Docs](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/extend-cloud-agent-with-mcp)
- [MCP Servers Repo](https://github.com/modelcontextprotocol/servers)
- Related: [[github-copilot/Agents]] (custom agents), [[github-copilot/Skills]]

Last updated: 2026-04-08
