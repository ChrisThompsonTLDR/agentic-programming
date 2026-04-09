---
title: Deep Wiki Plugin
github_url: https://github.com/microsoft/skills/tree/main/.github/plugins/deep-wiki
repo_url: https://github.com/microsoft/skills
stars: 2000
forks: 218
latest_commit: 67ae723a23ba880e3e5c8a3e5e2320092024476e (2026-04-02: Move package field into metadata map)
tags: [copilot-plugins, deep-wiki, documentation, vitepress, mermaid, agents, skills, onboarding]
related: [[github-copilot/Plugins]], [[github-copilot/Skills]], [[Skills/Skill Creator]], [[Agent Sync]]
---

# Deep Wiki Plugin

![Deep Wiki Badge](https://github.com/microsoft/skills/raw/main/.github/plugins/deep-wiki/badge.png)

**AI-Powered Wiki Generator for Code Repositories — GitHub Copilot CLI Plugin**

Generate comprehensive, structured, Mermaid-rich documentation wikis for any codebase — with dark-mode VitePress sites, onboarding guides, and deep research capabilities. Distilled from [OpenDeepWiki/deepwiki-open](https://github.com/OpenDeepWiki/deepwiki-open).

## Installation

### From Marketplace (Recommended)
```
# Inside Copilot CLI
/plugin marketplace add microsoft/skills
/plugin install deep-wiki@skills
```

### Local Install
```
copilot --plugin-dir ./deep-wiki
```

## Commands

| Command | Description |
|---------|-------------|
| `/deep-wiki:generate` | Generate complete wiki — catalogue + all pages + onboarding guides + VitePress site |
| `/deep-wiki:crisp` | Fast wiki generation — concise, parallelized, rate-limit-friendly (5-8 pages) |
| `/deep-wiki:catalogue` | Generate structured JSON table-of-contents |
| `/deep-wiki:page <topic>` | Single page with dark-mode Mermaid diagrams |
| `/deep-wiki:research <topic>` | Deep research with zero tolerance for shallow analysis |
| `/deep-wiki:changelog` | Changelog analysis |
| `/deep-wiki:ask <question>` | Q&A over repo |
| `/deep-wiki:onboard` | Onboarding guide |
| `/deep-wiki:agents` | AGENTS.md for MCP discovery |
| `/deep-wiki:llms` | llms.txt for LLM integration |
| `/deep-wiki:ado` | Azure DevOps integration |
| `/deep-wiki:build` | Build wiki site |
| `/deep-wiki:deploy` | Deploy to GitHub Pages/Netlify |
| `/deep-wiki:mcp` | MCP server config |

View agents: `/agents`

## Agents

| Agent | Description |
|-------|-------------|
| `wiki-architect` | Analyzes repos, generates structured catalogues + onboarding architecture |
| `wiki-writer` | Generates pages with dark-mode Mermaid diagrams and deep citations |
| `wiki-researcher` | Deep research with evidence-first approach |

## Skills (Auto-Invoked)

| Skill | Triggers When |
|-------|---------------|
| `wiki-architect` | Create wiki/document repo/map codebase |
| `wiki-page-writer` | Document component/technical deep-dive |
| `wiki-changelog` | Recent changes/changelog |
| `wiki-researcher` | In-depth investigation |
| `wiki-onboarding` | New user guides |
| `wiki-vitepress` | VitePress site generation |
| `wiki-llms-txt` | LLM integration files |
| `wiki-agents-md` | AGENTS.md generation |
| `wiki-mermaid-dark` | Dark-mode diagrams |
| `wiki-mcp-config` | MCP server setup |

## Design Principles (12 Rules)

1. **Source Citations**: Every claim links to code/commit.
2. **Structure-First**: TOC before content.
3. **Evidence-Based**: No speculation.
4. **Diagram-Rich**: Mermaid for architecture flows.
5. **Dark-Mode Native**: VitePress with dark theme.
6. **Onboarding-Focused**: New dev guides first.
7. **llms.txt/AGENTS.md**: MCP discovery.
8. **Rate-Limit Friendly**: Parallel/concise modes.
9. **Multi-Turn Research**: Iterative deepening.
10. **JSON Catalogues**: Machine-readable TOC.
11. **Single-Page Deep Dives**: Focused topics.
12. **Deployment-Ready**: Build/deploy commands.

## Plugin Structure

```
.github/plugins/deep-wiki/
├── .claude-plugin/          # Claude integration
├── commands/                # CLI commands
├── skills/                  # Auto-skills
├── agents/                  # Agent profiles
├── README.md                # Full docs
└── references/              # Examples/templates
```

## MCP Integration

Generates:
- `llms.txt`: LLM tool discovery.
- `AGENTS.md`: Agent paths/methods table.

| Path | Method | Tools |
|------|--------|-------|
| /wiki/catalogue | POST | read, search |
| /wiki/page | POST | edit, write |

## Resources
- [GitHub Repo](https://github.com/microsoft/skills/tree/main/.github/plugins/deep-wiki)
- [Full README](https://github.com/microsoft/skills/blob/main/.github/plugins/deep-wiki/README.md)
- [Copilot Plugins Guide]([[github-copilot/Plugins]])
- [Skills Guide]([[github-copilot/Skills]])

Last updated: 2026-04-08
