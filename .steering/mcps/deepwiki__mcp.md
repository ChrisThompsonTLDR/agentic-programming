---
name: deepwiki-mcp
owner: deepwiki
url: https://docs.devin.ai/work-with-devin/deepwiki-mcp
product_url: https://deepwiki.com
mcp_url: https://mcp.deepwiki.com/
type: official
transport: both
language: other
version:
stars:
last_updated: 2026-04-08
tags: [mcp, deepwiki, devin, documentation, github, remote-mcp, http]
---

# DeepWiki MCP

> Free, remote MCP access to DeepWiki’s public GitHub repo documentation and Ask Devin–style Q&A—no API key for public repos.

## What It Does

The DeepWiki MCP server exposes DeepWiki’s generated wikis and search so agents can list topics, read wiki pages, and ask grounded questions about **public** repositories. **Private** repos require Devin’s hosted MCP with a bearer token ([Devin docs](https://docs.devin.ai/work-with-devin/deepwiki-mcp)). The service is advertised from [mcp.deepwiki.com](https://mcp.deepwiki.com/) with full setup on [docs.devin.ai](https://docs.devin.ai/work-with-devin/deepwiki-mcp).

## Tools / Resources / Prompts

| Name | Type | Description |
|------|------|-------------|
| `read_wiki_structure` | tool | List documentation topics for a GitHub repository. |
| `read_wiki_contents` | tool | Read wiki content for a GitHub repository. |
| `ask_question` | tool | Ask a question about a repo; AI answer grounded in DeepWiki context. |

No separate **resources** or **prompts** are documented on the official DeepWiki MCP page as of the research date.

## Installation

**Public repos (Streamable HTTP, recommended):** no local install; point the client at the remote endpoint.

```bash
# Claude Code (from mcp.deepwiki.com landing)
claude mcp add -s user -t http deepwiki https://mcp.deepwiki.com/mcp
```

## Configuration

**Cursor / Windsurf-style** (per [Devin docs](https://docs.devin.ai/work-with-devin/deepwiki-mcp)—field name may vary by client: `serverUrl` vs `url`):

```json
{
  "mcpServers": {
    "deepwiki": {
      "serverUrl": "https://mcp.deepwiki.com/mcp"
    }
  }
}
```

**Alternative JSON** (as shown on [mcp.deepwiki.com](https://mcp.deepwiki.com/)):

```json
{
  "mcpServers": {
    "deepwiki": {
      "url": "https://mcp.deepwiki.com/mcp"
    }
  }
}
```

**Wire protocols** ([Devin docs](https://docs.devin.ai/work-with-devin/deepwiki-mcp)):

| Endpoint | URL | Notes |
|----------|-----|--------|
| Streamable HTTP (recommended) | `https://mcp.deepwiki.com/mcp` | Preferred; works with Cloudflare, OpenAI, Claude. |
| SSE (legacy) | `https://mcp.deepwiki.com/sse` | Deprecated; avoid for new setups. |

**Private repositories** ([mcp.deepwiki.com](https://mcp.deepwiki.com/)):

```json
{
  "mcpServers": {
    "deepwiki": {
      "url": "https://mcp.devin.ai/mcp",
      "headers": {
        "Authorization": "Bearer <API_KEY>"
      }
    }
  }
}
```

## Authentication / Environment Variables

| Variable | Required | Description |
|----------|----------|-------------|
| (none) | no | Public DeepWiki MCP at `mcp.deepwiki.com` requires no auth for public GitHub repos. |
| Devin API key | yes (private) | Bearer token in `Authorization` header when using `https://mcp.devin.ai/mcp` for private repos. |

## Notes

- **Product surface:** [deepwiki.com](https://deepwiki.com) is the user-facing wiki browser; **MCP** is hosted at [mcp.deepwiki.com](https://mcp.deepwiki.com/).
- **Docs:** Canonical instructions live under Devin documentation, not only on the wiki site.
- **Related:** [Devin MCP marketplace](https://docs.devin.ai/work-with-devin/mcp), [OpenAI remote MCP guide](https://platform.openai.com/docs/guides/tools-remote-mcp) (linked from Devin docs).
