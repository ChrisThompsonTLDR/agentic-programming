# Unified Constraints and Guardrails

This file defines universal prohibitions and compliance rules for all Task-Master commands, MCPs, and personas.  
Every command must **read this file at startup** and enforce all constraints before performing any action.

---

## Global Principles
- **Truth over assumption:** all data must trace to PRD, task metadata, or explicit user input.  
- **No invention:** AI must never create new requirements, dependencies, or code without traceable reference.  
- **Local-first:** all writes and operations occur inside the project workspace.  
- **Non-destructive:** commands must not modify unrelated tasks, branches, or data.

---

## Forbidden Actions

### 1. Scope and Time
- ❌ Do not make or imply **time estimates**.  
- ❌ Do not invent **scope**, features, or requirements.  
- ❌ Do not silently add **dependencies** or external references.  
- ❌ Do not expand tasks beyond their defined boundaries.

### 2. Code Generation and Expansion
- ❌ No code emission in any `expand-*` file.  
- ❌ `expand-*` commands may only output **subtasks** with PRD traceability.  
- ❌ Do not generate boilerplate, migrations, controllers, or configs during planning.

### 3. Output Formatting
- ❌ Never include "Next steps," "Recommendations," or "To do next" in command output.  
- ✅ Output only the information required by downstream personas.  
- ✅ Follow the **step index header** and file structure defined in `00-index.md`.

### 4. Security and Secrets
- ❌ Never expose real credentials, tokens, or API keys.  
- ✅ Reference environment variables only (e.g., `SENTRY_DSN`, `MEILISEARCH_KEY`).  
- ❌ Do not read or transmit private repository data unless explicitly scoped in MCP config.  
- ❌ Do not store secrets in `.cursor/commands` or generated markdown.

### 5. MCP Interaction
- ✅ All orchestration must go through **MCP tools**.  
- ❌ Do not call Task-Master or system CLIs directly from markdown templates.  
- ❌ Do not proceed if required MCP servers are unavailable — stop and report the failure.

### 6. Knowledge and Documentation
- ✅ All subtasks must include PRD line references and applicable gates (testing, quality, perf, security).  
- ✅ All commands must reference this `01-forbidden.md`.  
- ❌ Do not overwrite or delete existing documentation files without explicit user approval.  
- ❌ Do not merge or collapse epics; maintain one folder per epic.

### 7. Metrics and Validation
- ✅ Use project gates as constants:  
  - Pint: clean  
  - Larastan: level ≥6 or baseline with zero new errors  
  - Mutation: ≥70%  
  - Pulse: p95 ≤500 ms, ≤10 queries  
  - Sentry: 0 unhandled exceptions, release recorded  
- ❌ Do not change thresholds inside command files — override only through config.

---

## Enforcement
Any command found violating these rules must:
1. Halt execution immediately.  
2. Log the rule violated and context.  
3. Output only:  
```

❌ Forbidden action detected — see 01-forbidden.md

```
4. Exit without performing side effects.
