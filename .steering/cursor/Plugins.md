---
title: Cursor Plugins
url: https://cursor.com/docs/plugins
tags: [cursor, plugins, marketplace, manifest, skills, rules]
related:
  - "[[cursor/Rules]]"
  - "[[cursor/Skills]]"
  - "[[cursor/Hooks]]"
  - "[[cursor/Agents]]"
  - "[[github-copilot/Skills]]"
---

# Cursor Plugins

**Official reference:** [Plugins | Cursor Docs](https://cursor.com/docs/plugins) · **Creating plugins:** [§ Creating plugins](https://cursor.com/docs/plugins#creating-plugins) · **Manifest & schema:** [Plugins reference](https://cursor.com/docs/reference/plugins)

Plugins are **distributable bundles** that package **rules**, **skills**, **agents**, **commands**, **MCP servers**, and **hooks** so teams can share one installable unit. Discovery: [Cursor Marketplace](https://cursor.com/marketplace) (official, reviewed) and [cursor.directory](https://cursor.directory) (community / MCP listings).

## What a plugin can contain

| Component | Role |
|-----------|------|
| **Rules** | Persistent guidance (`.mdc` under `rules/`) |
| **Skills** | Packaged agent capabilities (`skills/<name>/SKILL.md`) |
| **Agents** | Custom agent definitions |
| **Commands** | Agent-executable command files |
| **MCP servers** | MCP configuration (e.g. `mcp.json`) |
| **Hooks** | Hook automation wired like project hooks |

Components are **discovered** from conventional folders unless the manifest overrides paths (see the reference doc).

## Layout (minimal mental model)

From Cursor’s docs and [plugin template](https://github.com/cursor/plugin-template):

```text
my-plugin/
├── .cursor-plugin/
│   └── plugin.json          # required manifest (at least `name`)
├── rules/
│   └── coding-standards.mdc
├── skills/
│   └── code-reviewer/
│       └── SKILL.md
└── mcp.json                 # optional, when bundling MCP
```

**Manifest example** (only `name` is required; more fields for marketplace metadata):

```json
{
  "name": "my-plugin",
  "description": "Custom development tools",
  "version": "1.0.0",
  "author": { "name": "Your Name" }
}
```

For **multi-plugin repos**, Cursor documents a **`.cursor-plugin/marketplace.json`** at the repo root. Submission: [cursor.com/marketplace/publish](https://cursor.com/marketplace/publish).

## Local development

1. Put the plugin under **`~/.cursor/plugins/local/<plugin-name>/`** with **`.cursor-plugin/plugin.json`** at that folder’s root.
2. **Restart** Cursor or **Developer: Reload Window**.
3. For fast iteration, **symlink** your repo into `~/.cursor/plugins/local/`.

Security note: marketplace plugins are **manually reviewed** and expected to be **open source**; see [Marketplace security](https://cursor.com/help/security-and-privacy/marketplace-security).

## Team / Enterprise marketplaces

On **Teams** and **Enterprise**, admins can add **team marketplaces** (import a GitHub repo, assign **required** vs **optional** plugins to distribution groups). **Enterprise** can use **SCIM**-synced groups. Flow: **Dashboard → Settings → Plugins → Team Marketplaces**. Example template repo: [fieldsphere/cursor-team-marketplace-template](https://github.com/fieldsphere/cursor-team-marketplace-template).

## Install & runtime notes

- **Scopes:** Plugins can be **project-scoped** or **user-level** (per docs).
- **MCP:** Toggle bundled servers under **Settings → Features → Model Context Protocol**. **Install deeplinks:** [MCP install links](https://cursor.com/docs/mcp/install-links) (`cursor://…/mcp/install?…`).
- **Rules / skills:** Managed under **Rules** in Settings (Always / Agent Decides / Manual); skills also **`/skill-name`** in chat.
- **Extensions:** `vscode.cursor.plugins.registerPath()` can register plugin directories from a VS Code extension (see docs § Using the Extension API).

## How this repo relates to plugins

| Topic | In this repository |
|--------|---------------------|
| **Cursor plugin bundle** | There is **no** committed **`my-plugin/.cursor-plugin/`** tree here. Capabilities are maintained as **steering sources** (e.g. **`.steering/skills/`**, **`.steering/agents/`**) and **mirrored** into **`.cursor/`** / **`.github/`** by sync rules — that is **repo layout**, not a Marketplace plugin zip/git product. |
| **Overlap** | If you later **publish** a plugin, you can reuse the same **SKILL.md** / agent shapes; compare with **`.steering/templates/skill.md`** and **`.steering/agents/sync-agents.md`**. |
| **Copilot skills** | GitHub’s cloud “skills” story is separate; see **`.steering/github-copilot/Skills.md`** for how this repo thinks about Copilot vs local Cursor assets. |

## Related in this repo

| File | Why |
|------|-----|
| `.steering/cursor/Rules.md` | Rules often ship inside plugins (`rules/*.mdc`). |
| `.steering/cursor/Hooks.md` | Hooks can be bundled; project hooks also use `.cursor/hooks.json`. |
| `.steering/cursor/Agents.md` | Agents can be bundled as plugin components. |
| `.steering/skills/sync-skills/SKILL.md` (or `agents/sync-skills.md`) | How **steering** replicates skills/agents into IDE paths (parallel concern to “install a plugin”). |
| `.steering/github-copilot/Skills.md` | Copilot cloud skills vs Cursor plugin skills. |

## Resources

- [Plugins](https://cursor.com/docs/plugins) — marketplace, teams, install, creating plugins.
- [Plugins reference](https://cursor.com/docs/reference/plugins) — full manifest, paths, checklist.
- [Plugin template (GitHub)](https://github.com/cursor/plugin-template) — starter tree.
- [Publish](https://cursor.com/marketplace/publish) — submission.
