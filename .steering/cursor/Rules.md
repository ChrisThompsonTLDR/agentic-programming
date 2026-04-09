---
title: Cursor Rules
url: https://cursor.com/docs/rules
tags: [cursor, rules, project-rules, agents-md, context]
related:
  - "[[cursor/Agents]]"
  - "[[cursor/Skills]]"
  - "[[cursor/Hooks]]"
  - "[[cursor/Plugins]]"
  - "[[github-copilot/Agents]]"
---

# Cursor Rules

**Official reference:** [Rules | Cursor Docs](https://cursor.com/docs/rules)

**Rules** inject **persistent, reusable instructions** into the **Agent (Chat)** context. They are not “memory” for the model; they are **prepended** (or selectively included) so the agent gets consistent project or org guidance.

**Important:** Per Cursor’s docs, rules **do not** apply to **Cursor Tab** (inline completions) or other non–Agent Chat surfaces. **User Rules** also **do not** apply to **Inline Edit (Cmd/Ctrl+K)**.

## The four rule sources

| Kind | Where | Notes |
|------|--------|--------|
| **Project rules** | **`.cursor/rules/`** | Version-controlled; `.md` or **`.mdc`** (frontmatter for `description`, `globs`, `alwaysApply`). |
| **User rules** | **Cursor Settings → Rules** | Global across projects; good for tone and personal defaults. |
| **Team rules** | **Cursor dashboard** (Team / Enterprise) | Org-wide; can be **enforced**; supports optional **glob** scoping. |
| **`AGENTS.md`** | Project **root** and/or **nested** dirs | Plain markdown, no rule frontmatter; simpler alternative to `.cursor/rules`. |

**Precedence** when guidance conflicts: **Team Rules → Project Rules → User Rules** (earlier wins). All applicable rules are **merged**.

## Project rules (`.cursor/rules`)

**Purpose:** Domain knowledge, architecture choices, workflows, and standards **specific to this codebase**.

**Layout** (from Cursor docs):

```text
.cursor/rules/
  react-patterns.mdc     # frontmatter: description, globs, alwaysApply
  api-guidelines.md      # simple markdown
  frontend/
    components.md
```

### How a rule is applied (rule “type”)

Controlled via the UI (type dropdown) mapping to **`description`**, **`globs`**, **`alwaysApply`**:

| Mode | Behavior |
|------|-----------|
| **Always Apply** | Every Agent chat in the project. |
| **Apply Intelligently** | Agent uses **`description`** to decide relevance. |
| **Apply to Specific Files** | When context matches **`globs`**. |
| **Apply Manually** | When **`@`-mentioned** in chat (e.g. `@my-rule`). |

### Frontmatter example

```markdown
---
description: "Standards for frontend components and API validation"
alwaysApply: false
---

- Use …
```

With **`.mdc`**, you can also set **`globs:`** for path-scoped rules (see official doc for full shape).

### Creating rules

- Chat: **`/create-rule`** — Agent drafts the file under **`.cursor/rules/`**.
- Settings: **Cursor Settings → Rules, Commands → + Add Rule**.

## `AGENTS.md`

- Place at **repo root** (and optionally in **subdirectories**) for **directory-scoped** stacking; nested files combine with parents, **more specific wins**.
- **No** rule frontmatter — just readable markdown sections (style, architecture, commands to prefer, etc.).
- Cursor positions this as a **lighter** option when **`.cursor/rules`** is more than you need.

**This repository** does not currently commit a root **`AGENTS.md`**; if you add one, keep it focused and point to canonical docs (e.g. **`.steering/README.md`**) instead of duplicating long policy.

## Team rules (summary)

Admins manage rules in the **dashboard**; options include **enable immediately**, **enforce** (users cannot disable), and **glob** patterns (e.g. `**/*.py`) to limit scope. Team rules apply **across repos** for that team when enabled. See [Enterprise](https://cursor.com/docs/enterprise) and the Rules doc § Team Rules.

## Importing rules

**Remote rules (GitHub):** **Settings → Rules, Commands → + Add Rule → Remote Rule (GitHub)** with a repo URL; Cursor **syncs** updates from the remote.

## Best practices (from Cursor)

- Keep rules **short** (under **~500 lines**); split into composable files.
- Prefer **references** (`@file.ts`) over pasting large bodies that go stale.
- Avoid duplicating generic tool knowledge (npm, git, pytest) or whole style guides—use **linters** where appropriate.
- **Commit** project rules so the team shares them; iterate when the agent repeats the same mistake.

## How this repo relates to rules

| Topic | In this repository |
|--------|---------------------|
| **`.cursor/rules/`** | Not present in the committed tree today. Add it when you want **path-scoped** or **@mention** rules alongside mirrored **skills** and **agents**. |
| **Steering** | Long-form human docs and templates live under **`.steering/`** (e.g. **`.steering/cursor/*.md`**, **`.steering/templates/`**). That is **documentation and source-of-truth text**, not automatically loaded as Cursor Rules unless you copy or symlink into **`.cursor/rules/`** or summarize into **`AGENTS.md`**. |
| **Plugins** | Rules can ship inside a **plugin** (`rules/*.mdc`); see **`.steering/cursor/Plugins.md`**. |
| **Hooks** | **Hooks** observe/control the loop; **rules** shape prompt content. Complementary; see **`.steering/cursor/Hooks.md`**. |

## Related in this repo

| File | Why |
|------|-----|
| `.steering/cursor/Agents.md` | Subagents vs **skills** vs rules — different mechanisms. |
| `.steering/cursor/Plugins.md` | Bundling rules for distribution. |
| `.steering/github-copilot/Agents.md` | Copilot’s `.github/agents/` story vs Cursor rules + agents. |
| User **create-rule** skill (if you install one) | Some teams use a packaged skill to scaffold **`.cursor/rules`** files; this repo does not ship that skill by default. |

## Resources

- [Rules](https://cursor.com/docs/rules) — types, frontmatter, AGENTS.md, Team Rules, FAQ.
- [Enterprise](https://cursor.com/docs/enterprise) — team content and enforcement context.
- [Plugins](https://cursor.com/docs/plugins) — shipping rules in plugins.
