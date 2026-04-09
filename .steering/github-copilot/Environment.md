---
title: Customizing Copilot Cloud Agent Environment
url: https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/customize-the-agent-environment
feature_status: GA
tags: [copilot, agents, environment, github-actions, runners]
related:
 - [[Github Copilot/Agents]]
 - [[Github Copilot/Agent MCP]]
 - [[Github Copilot/Skills]]
---

# Customizing the Development Environment for GitHub Copilot Cloud Agent

Copilot cloud agent runs in an **ephemeral GitHub Actions environment** (Ubuntu Linux by default) to explore code, build, test, lint, etc.

Customize via **`.github/workflows/copilot-setup-steps.yml`**—runs **before** agent starts.

## copilot-setup-steps.yml Structure

```yaml
# Triggers: manual, push/PR to this file
on:
  workflow_dispatch:
  push:
    paths: [.github/workflows/copilot-setup-steps.yml]
  pull_request:
    paths: [.github/workflows/copilot-setup-steps.yml]

jobs:
  copilot-setup-steps:  # MUST be this name
    runs-on: ubuntu-latest  # or larger/self-hosted/Windows
    permissions:  # Minimal needed
      contents: read
    steps:
      - uses: actions/checkout@v4
      # Your setup steps here
```

## Preinstall Dependencies/Tools

Speed up agent—install deps reliably:

```yaml
steps:
  - uses: actions/checkout@v4
  - uses: actions/setup-node@v4
    with:
      node-version: 20
      cache: npm
  - run: npm ci
```

## Runners

| Type | Config | Benefits |
|------|--------|----------|
| **Standard** | `ubuntu-latest` | Default |
| **Larger** | `ubuntu-4-core` (org setup req.) | More CPU/RAM/disk |
| **Self-hosted** | `arc-scale-set-name` | Internal network, match CI |
| **Windows** | `windows-latest` | Windows toolchain |

**Note**: Ubuntu x64/Windows 64-bit only. Ephemeral/single-use recommended.

## Git LFS

```yaml
- uses: actions/checkout@v4
  with:
    lfs: true
```

## Environment Variables/Secrets

Set in repo **copilot environment** (Settings > Environments > New: `copilot`):

- Vars: `MY_VAR=value`
- Secrets: `MY_SECRET`

Access: `${{ env.MY_VAR }}` / `${{ secrets.MY_SECRET }}`

Proxy example:

| Var | Example |
|-----|---------|
| `https_proxy` | `http://proxy.corp:8080` |
| `no_proxy` | `localhost,127.0.0.1` |

## Resources
- [Docs](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/customize-the-agent-environment)
- [Firewall](https://docs.github.com/en/copilot/how-tos/use-copilot-agents/cloud-agent/customize-the-agent-firewall)

[[GitHub Copilot]]
