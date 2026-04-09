---
title: GitHub Agentic Workflows
url: https://github.blog/ai-and-ml/automate-repository-tasks-with-github-agentic-workflows/
feature_status: Technical preview
tags:
  - github-copilot
  - agentic-workflows
  - github-actions
  - continuous-ai
  - gh-aw
related:
  - "[[github-copilot/Agents]]"
  - "[[github-copilot/Skills]]"
  - "[[github-copilot/Settings]]"
gh_aw_hub: https://github.github.com/gh-aw/
---

# GitHub Agentic Workflows

**Primary announcement:** [Automate repository tasks with GitHub Agentic Workflows](https://github.blog/ai-and-ml/automate-repository-tasks-with-github-agentic-workflows/) (GitHub Blog, Feb 2026)

**Product / docs hub:** [github.github.com/gh-aw](https://github.github.com/gh-aw/?utm_source=blog-agentic-workflows-cta&utm_medium=blog&utm_campaign=agentic-workflows-tech-preview-feb-2026)

Agentic Workflows are **intent-driven automations** that run on **GitHub Actions** using **coding agents**. You author **plain Markdown** (plus YAML frontmatter) checked into **`.github/workflows/`**; GitHub compiles a paired **lock file** and executes the run with **sandboxing**, **tool allowlists**, and **safe outputs** so repository changes stay **reviewable**.

They are **not** a replacement for deterministic **CI/CD** (build, test, release). They extend automation to **subjective, repetitive** repo work—triage, docs drift, test gaps, CI triage, reports—alongside existing YAML workflows.

## Mental model

| Idea | Detail |
|------|--------|
| **Authoring** | Markdown describes **goals**; frontmatter pins **triggers**, **permissions**, **tools**, and **safe outputs**. |
| **Execution** | Standard **GitHub Actions** infrastructure: logging, auditing, permissions, isolation. |
| **Engines** | Configurable **coding agent** backends (e.g. **Copilot CLI**, **Claude Code**, **OpenAI Codex**) per [engines reference](https://github.github.com/gh-aw/reference/engines/). |
| **Outputs** | Writes default to **read-only**; mutating GitHub effects go through **safe outputs** (e.g. open a PR, comment on an issue)—mapped, pre-approved-style operations—not silent repo mutation. |

Official **security / threat model:** [Architecture introduction](https://github.github.com/gh-aw/introduction/architecture/).

## Files on disk

For each workflow you typically commit **two** files under **`.github/workflows/`**:

1. **`*.md`** — Agentic workflow spec: YAML frontmatter (`on`, `permissions`, `safe-outputs`, `tools`, …) + Markdown instructions for the agent.
2. **`*.lock.yml`** — Generated **lock** file Actions runs; produced by the **`gh-aw`** tooling (see [Quick start](https://github.github.io/gh-aw/setup/quick-start/), [Creating workflows](https://github.github.io/gh-aw/setup/creating-workflows/)).

Blog example names: `daily-repo-status.md` and `daily-repo-status.lock.yml`.

**Tooling (high level):** install the **`gh-aw`** extension (`gh extension install github/gh-aw`), use **`gh aw compile`** (and related commands) after editing the Markdown spec so the lock file stays in sync.

## “Meet the Workflows” series (pattern library)

Deep dives from the **Agentic Workflows** / **Peli’s Agent Factory** series—useful as **templates and vocabulary** when designing your own `.md` specs:

| Theme | Article |
|--------|---------|
| **Issues / triage** | [Meet the Workflows](https://github.github.com/gh-aw/blog/2026-01-13-meet-the-workflows/) (summarize, label, route) |
| **Documentation** | [Meet the Workflows: Continuous Documentation](https://github.github.com/gh-aw/blog/2026-01-13-meet-the-workflows-documentation/) |
| **Code simplification** | [Continuous simplicity](https://github.github.com/gh-aw/blog/2026-01-13-meet-the-workflows-continuous-simplicity/) |
| **Testing & validation** | [Testing & validation](https://github.github.com/gh-aw/blog/2026-01-13-meet-the-workflows-testing-validation/) |
| **Quality / CI hygiene** | [Quality hygiene](https://github.github.com/gh-aw/blog/2026-01-13-meet-the-workflows-quality-hygiene/) |

The announcement also links **issue triage**, **metrics / reporting**, and **Continuous AI** ([GitHub Next — Continuous AI](https://githubnext.com/projects/continuous-ai/)).

**Workflow gallery / factory tour:** [Welcome to Peli’s Agent Factory](https://github.github.com/gh-aw/blog/2026-01-12-welcome-to-pelis-agent-factory/) (also cited from [workflow gallery](https://github.github.io/gh-aw/blog/2026-01-12-welcome-to-pelis-agent-factory/)).

## Guardrails (why this isn’t “raw agent in Actions”)

Compared to running a generic agent CLI inside a normal job, Agentic Workflows emphasize:

- **Read-only by default**; elevated effects via **safe outputs**.
- **Sandboxing**, **tool allowlisting**, **network isolation** (see architecture doc).
- **No automatic merge** of PRs—humans stay in the loop for integration.

Treat workflow Markdown **as code**: review diffs, keep specs focused, evolve deliberately.

## Billing and accounts

Workflow runs use **coding agents** at runtime and incur **costs**. With **Copilot** default settings, the blog describes about **two [Copilot premium requests](https://docs.github.com/en/billing/concepts/product-billing/github-copilot-premium-requests)** per run (agent work + guardrail path through safe outputs)—verify current docs for your plan. Other engines: see **[engines](https://github.github.com/gh-aw/reference/engines/)** for tokens and secrets.

## Team practices (from the announcement)

- Start with **low-risk** safe outputs (comments, drafts, reports) before broad **PR** creation.
- Prefer **goal-oriented** maintenance (refactors, tests, simplification) over unsupervised **feature** work.
- Be explicit in instructions: **format**, **tone**, **links**, **when to stop**.
- Add **secrets** your chosen engine needs (see engines doc).

## How this repo relates

| Topic | In this repository |
|--------|---------------------|
| **Agentic Workflows (`gh-aw`)** | **Not** the same as the **steering sync** workflow in **`.github/workflows/verify-steering-sync.yml`**, which is ordinary Actions + shell/Python to mirror **`.steering/`** into IDE paths. |
| **Copilot agents** | Custom **`.github/agents/*.agent.md`** profiles are documented in **`.steering/github-copilot/Agents.md`**; they address **IDE / Copilot Chat / cloud agent** usage, not necessarily `gh-aw` Markdown workflow files. |
| **Adoption** | If you add Agentic Workflows here, store **`.md` + `.lock.yml`** under **`.github/workflows/`**, document **secrets** and **safe outputs** in the PR, and link this note for reviewers. |

## Learn more (official)

- [Documentation hub](https://github.github.com/gh-aw/)
- [How they work](https://github.github.io/gh-aw/introduction/how-they-work/)
- [Quick start](https://github.github.io/gh-aw/setup/quick-start/)
- [Creating workflows](https://github.github.io/gh-aw/setup/creating-workflows/)
- [Community feedback](https://gh.io/aw-tp-community-feedback) · [GitHub Next Discord — #agentic-workflows](https://gh.io/next-discord)

**Prompt helper (from blog):** use your coding agent with instructions from [`github/gh-aw` `create.md`](https://github.com/github/gh-aw/blob/main/create.md) to scaffold a new workflow.
