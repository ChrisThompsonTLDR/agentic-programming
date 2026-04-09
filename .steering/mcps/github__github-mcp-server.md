---
name: github-mcp-server
owner: github
url: https://github.com/github/github-mcp-server
docs_url: https://docs.github.com/en/copilot/how-tos/provide-context/use-mcp/set-up-the-github-mcp-server
hosted_url: https://api.githubcopilot.com/mcp/
type: official
transport: both
language: Go
version: v0.32.0
stars: 28674
last_updated: 2026-04-08
tags: [mcp, github, copilot, remote-mcp, issues, pull-requests, actions, repository]
---

# GitHub MCP Server (hosted)

> Official GitHub MCP server: connect agents to repos, issues, PRs, Actions, security, Copilot features, and more—via **GitHub-hosted HTTP** or a **local** stdio/Docker binary.

## What It Does

The **remote** server runs at **`https://api.githubcopilot.com/mcp/`** and is the recommended path when your MCP host supports remote servers (VS Code 1.101+, Cursor, Claude Desktop, Windsurf, Copilot in other IDEs, etc.). Auth is **OAuth** (per-host GitHub App) or a **GitHub PAT** in the `Authorization` header. The same capabilities are implemented in the open-source **[github/github-mcp-server](https://github.com/github/github-mcp-server)** (Go); hosted vs local differs only in transport and how you authenticate. Some tools inherit **Copilot or paid-feature** requirements ([GitHub Docs](https://docs.github.com/en/copilot/how-tos/provide-context/use-mcp/set-up-the-github-mcp-server)).

## Tools / Resources / Prompts

Capabilities are grouped into **toolsets** (each toolset exposes many MCP tools). When no toolsets are configured on the remote server, **defaults** apply ([README](https://github.com/github/github-mcp-server/blob/main/README.md)).

| Name | Type | Description |
|------|------|-------------|
| `context` | toolset | Current user and GitHub context (**strongly recommended**). |
| `repos` | toolset | Repository browse/search, files, metadata. |
| `issues` | toolset | Issues. |
| `pull_requests` | toolset | Pull requests. |
| `actions` | toolset | GitHub Actions workflows, runs, jobs, artifacts. |
| `code_security` | toolset | Code scanning and related security APIs. |
| `dependabot` | toolset | Dependabot. |
| `discussions` | toolset | Discussions. |
| `gists` | toolset | Gists. |
| `git` | toolset | Low-level Git API operations. |
| `labels` | toolset | Labels. |
| `notifications` | toolset | Notifications. |
| `orgs` | toolset | Organizations. |
| `projects` | toolset | Projects. |
| `secret_protection` | toolset | Secret scanning. |
| `security_advisories` | toolset | Security advisories. |
| `stargazers` | toolset | Stargazers. |
| `users` | toolset | Users. |
| `copilot` | toolset | Copilot-related tools (e.g. coding agent); **extra on remote**. |
| `copilot_spaces` | toolset | Copilot Spaces; **remote**. |
| `github_support_docs_search` | toolset | Search GitHub product/support docs; **remote**. |

**Remote-only / advanced:** **Insiders** early features via URL `https://api.githubcopilot.com/mcp/insiders` or header `X-MCP-Insiders: true` ([README](https://github.com/github/github-mcp-server/blob/main/README.md)). **Dynamic toolsets** (`enable_toolset`, `list_available_toolsets`, etc.) are documented for the **local** binary/Docker; behavior on hosted follows [remote server docs](https://github.com/github/github-mcp-server/blob/main/docs/remote-server.md).

For a **full per-tool list** (e.g. `actions_list`, `get_file_contents`, …), see the **Tools** section of the [repository README](https://github.com/github/github-mcp-server/blob/main/README.md).

## Installation

**Hosted (no local binary):** add the server URL to your MCP client; complete OAuth in the host or supply a PAT (see Configuration).

**Local (Docker)** — optional alternative from upstream README:

```bash
docker run -i --rm -e GITHUB_PERSONAL_ACCESS_TOKEN ghcr.io/github/github-mcp-server
```

## Configuration

**VS Code / common JSON (OAuth-friendly):** `type: http` + URL ([README](https://github.com/github/github-mcp-server/blob/main/README.md)):

```json
{
  "servers": {
    "github": {
      "type": "http",
      "url": "https://api.githubcopilot.com/mcp/"
    }
  }
}
```

**PAT on the hosted endpoint** (pattern from README / Visual Studio docs):

```json
{
  "servers": {
    "github": {
      "type": "http",
      "url": "https://api.githubcopilot.com/mcp/",
      "headers": {
        "Authorization": "Bearer YOUR_GITHUB_PAT"
      }
    }
  }
}
```

Some hosts use `requestInit.headers` instead of top-level `headers` ([GitHub Docs – Visual Studio example](https://docs.github.com/en/copilot/how-tos/provide-context/use-mcp/set-up-the-github-mcp-server)). Cursor-specific steps: [install-cursor.md](https://github.com/github/github-mcp-server/blob/main/docs/installation-guides/install-cursor.md) in the repo.

**GitHub Enterprise Cloud (ghe.com)** example shape from README: `https://copilot-api.<org>.ghe.com/mcp` with PAT header.

## Authentication / Environment Variables

| Mechanism | Required | Description |
|-----------|----------|-------------|
| OAuth | depends | Preferred for hosted server in supported hosts; scopes limited to what you approve ([GitHub Docs](https://docs.github.com/en/copilot/how-tos/provide-context/use-mcp/set-up-the-github-mcp-server)). |
| GitHub PAT | optional | `Authorization: Bearer <token>` for hosts without OAuth; scopes must match tools you use ([token docs](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token)). |
| `GITHUB_PERSONAL_ACCESS_TOKEN` | yes (local Docker) | Passed into container for **local** server ([README](https://github.com/github/github-mcp-server/blob/main/README.md)). |

Org/enterprise **“MCP servers in Copilot”** policy may apply ([GitHub Docs](https://docs.github.com/en/copilot/how-tos/provide-context/use-mcp/set-up-the-github-mcp-server)). Enterprise Managed Users may be PAT-restricted; OAuth app allowlists may apply per host.

## Notes

- **Registry / one-click:** Discover and install via [GitHub MCP Registry](https://github.com/mcp) (`@mcp github` in VS Code) per [GitHub Docs](https://docs.github.com/en/copilot/how-tos/provide-context/use-mcp/set-up-the-github-mcp-server).
- **GitHub Enterprise Server:** remote hosting not supported; use **local** server ([README](https://github.com/github/github-mcp-server/blob/main/README.md)).
- **Policies:** See [policies-and-governance.md](https://github.com/github/github-mcp-server/blob/main/docs/policies-and-governance.md) in the repo.
