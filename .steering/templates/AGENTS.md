# AGENTS.md

Project-wide instructions for AI coding agents (Cursor Agent, Claude Code, GitHub Copilot, and similar tools). **Copy this file to the repository root** as `AGENTS.md` and customize paths, product names, and links to match your project.

---

## Purpose

- Set **defaults** for how agents should work in this repo (investigate before guessing, match existing code style, keep diffs focused).
- Point agents at **skills** and **MCP servers** so they use structured playbooks and live tools instead of relying only on training data.

This file does **not** replace skills or MCP configuration; it **nudges** agents to discover and use them when they fit the task.

---

## Before you change code

1. **Read enough context** — open the files you will edit; follow local naming, patterns, and error handling.
2. **Prefer verified facts** — for APIs, SDKs, or product behavior, use **MCPs** or official docs rather than assuming from memory.
3. **Prefer skills for playbooks** — when the task matches a packaged skill’s `description`, **read that skill’s `SKILL.md`** (and any `references/` it points to) before improvising a workflow.

---

## Skills (use when relevant)

**Skills** are folders containing `SKILL.md` (YAML frontmatter + instructions). They are loaded progressively when the task matches the skill’s **`description`**, or when the user invokes them explicitly (e.g. `/skill-name` where supported).

| Typical locations (project) | Role |
|-----------------------------|------|
| `.cursor/skills/<name>/` | Cursor Agent |
| `.claude/skills/<name>/` | Claude Code (and compatibility with other tools) |
| `.github/skills/<name>/` | GitHub Copilot agent mode / cloud |

**How to use them**

- At the start of a task, **scan available skills** (metadata + descriptions) when your environment exposes them.
- If a skill clearly applies, **read `SKILL.md`** and follow it; do not claim you followed a skill you never opened.
- If this repo keeps a **steering** copy under `.steering/skills/<name>/`, treat that as canonical and keep IDE copies in sync per maintainer docs (e.g. sync-skills / CI).
- For **test-driven design** with Pest (red/green/refactor, grouping, mocks, browser and architecture tests, coverage), read `.steering/skills/sync-agents/tdd.md` when that matches the task.

**Good skill descriptions** include *what* the skill does and *when* to use it (trigger phrases). When authoring skills, optimize the `description` field for matching.

---

## MCP servers (use when appropriate)

**MCP** tools extend the agent with search, docs, browser, VCS, databases, and other integrations. Availability depends on the user’s editor or host configuration.

**When to use MCPs**

- **Documentation and APIs** — search official docs, read current signatures, confirm deprecations.
- **Web or repo facts** — fetch issues, releases, or pages when the answer must be current.
- **Specialized tools** — lint, test, or domain-specific servers when they reduce error or toil.

**How to use them well**

- **Inspect tool schemas** (names, required arguments) before calling; do not invent parameters.
- Prefer MCP-backed **fresh** information over stale model knowledge for version-sensitive work.
- If an MCP call fails, say what failed and fall back transparently (e.g. official docs URL, or ask the user).

If this repo documents configured servers (e.g. under `.steering/mcps/` or project README), **consult those notes** for capabilities and env vars.

---

## Custom agents / subagents

If the repo defines **custom agents** (e.g. `.cursor/agents/`, `.github/agents/`), use them when the user asks for that workflow or when the task matches their `description`. Agent files may include Copilot-only fields (e.g. `tools:`, `mcp-servers:`) in GitHub copies; other mirrors may strip those — follow the copy your runtime actually loads.

---

## Conventions (edit to taste)

- **Scope** — Change only what the user asked for; avoid drive-by refactors.
- **Evidence** — Run checks you cite (tests, linters); do not claim green without running them.
- **Secrets** — Never commit credentials; use environment variables and host-provided secret stores.

---

## Related templates and steering docs

| Path | Use |
|------|-----|
| `.steering/templates/skill.md` | Authoring packaged `SKILL.md` files |
| `.steering/templates/agent.md` | Extended **Core Principles** (optional reading; some agents embed this section) |
| `.steering/skills/sync-agents/tdd.md` | Test-Driven Design playbook (Pest, grouping, mocking, browser/arch tests, coverage / type coverage) |

Replace or extend the table above for your monorepo or single-package layout.
