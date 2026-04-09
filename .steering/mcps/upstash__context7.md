---
name: context7
owner: upstash
url: https://github.com/upstash/context7
product_url: https://context7.com
type: official
transport: both
language: TypeScript
version: 2.1.7
stars: 52032
last_updated: 2026-04-08
tags: [mcp, documentation, llm, libraries, npm, upstash]
---

# Context7

> Up-to-date, version-specific library documentation for LLMs and AI coding assistants, delivered via MCP tools, a hosted MCP endpoint, CLI (`ctx7`), and a REST API.

## What It Does

Context7 indexes community-contributed documentation for many libraries and frameworks so models can retrieve current APIs and examples instead of relying on stale training data. Integrations include **MCP** (local `npx` server or remote `https://mcp.context7.com/mcp`), **`npx ctx7 setup`** (OAuth, API key, optional skill install), and **direct API** use per [API guide](https://context7.com/docs/api-guide). This repository’s Copilot docs map the secret `CONTEXT7_KEY` to the **`CONTEXT7_API_KEY`** env var expected by the MCP package and hosted endpoint.

## Tools / Resources / Prompts

| Name | Type | Description |
|------|------|-------------|
| `resolve-library-id` | tool | Resolves a general library name to a Context7 library ID. Parameters (from upstream README): `query` (required) — user question/task for ranking; `libraryName` (required) — name to search. |
| `query-docs` | tool | Retrieves documentation for a library. Parameters (from upstream README): `libraryId` (required) — e.g. `/mongodb/docs`, `/vercel/next.js`; `query` (required) — question or task. |

No separate MCP **resources** or **prompts** are listed in the [project README](https://github.com/upstash/context7/blob/master/README.md) or [developer guide](https://context7.com/docs/resources/developer) as of the research date.

## Installation

**Hosted MCP (HTTP):** use server URL `https://mcp.context7.com/mcp` and authenticate with the `CONTEXT7_API_KEY` header (see [Manual installation / all clients](https://context7.com/docs/resources/all-clients)).

**Local MCP (stdio) via npm package:**

```bash
npx -y @upstash/context7-mcp
```

**Guided setup (OAuth + key + skill/MCP choice):**

```bash
npx ctx7 setup
```

Optional flags such as `--cursor`, `--claude`, or `--opencode` target a specific client ([README](https://github.com/upstash/context7/blob/master/README.md)).

## Configuration

**VS Code / generic `mcp.json` style (stdio + env)** — from [Developer Guide](https://context7.com/docs/resources/developer):

```json
{
  "mcpServers": {
    "context7": {
      "command": "npx",
      "args": ["-y", "@upstash/context7-mcp"],
      "env": {
        "CONTEXT7_API_KEY": "YOUR_API_KEY"
      }
    }
  }
}
```

**Local server flags** (same guide): `node packages/mcp/dist/index.js --transport stdio --api-key YOUR_API_KEY` or `--transport http --port 8080`. Default transport is `stdio`.

**This repo’s Copilot MCP example** uses the secret name `CONTEXT7_KEY` but passes it as `CONTEXT7_API_KEY` for the child process — align the **npm package name** with upstream: prefer `@upstash/context7-mcp`, not `@context7/mcp-server` (see [README.md](https://github.com/upstash/context7/blob/master/README.md) badges and docs).

## Authentication / Environment Variables

| Variable / header | Required | Description |
|-------------------|----------|-------------|
| `CONTEXT7_API_KEY` | Recommended | API key from [context7.com/dashboard](https://context7.com/dashboard); higher rate limits than without a key ([README](https://github.com/upstash/context7/blob/master/README.md)). |
| `CONTEXT7_API_KEY` (HTTP header) | For hosted MCP | Passed as a header when using `https://mcp.context7.com/mcp` ([README](https://github.com/upstash/context7/blob/master/README.md)). |
| `--api-key` | Optional CLI | Overrides env when both set ([Developer Guide](https://context7.com/docs/resources/developer)). |

**OAuth:** `npx ctx7 setup` performs OAuth and can generate an API key ([README](https://github.com/upstash/context7/blob/master/README.md)).

## Notes

- **Publisher:** [Upstash](https://github.com/upstash) on GitHub; product site [context7.com](https://context7.com). npm: [`@upstash/context7-mcp`](https://www.npmjs.com/package/@upstash/context7-mcp) (version **2.1.7** on npm `latest` as of 2026-04-08).
- **Pricing (public):** Free (1,000 API calls/month per [plans page](https://context7.com/plans)), Pro ($10/seat/month, 5,000 calls/seat), Enterprise (custom). Overage and private-repo parsing details are on the same page.
- **Scope of open source:** The repo hosts the **MCP server** source; API backend, parsing, and crawling are private ([README disclaimer](https://github.com/upstash/context7/blob/master/README.md)).
- **Quality:** Documentation is community-contributed; accuracy is not guaranteed ([README disclaimer](https://github.com/upstash/context7/blob/master/README.md)).
- **Alternatives / related:** CLI `ctx7 library` / `ctx7 docs` for non-MCP workflows; [REST API](https://context7.com/docs/api-guide) for custom integrations.
- **Verify tools:** `npx -y @modelcontextprotocol/inspector npx @upstash/context7-mcp` ([Developer Guide](https://context7.com/docs/resources/developer)).
