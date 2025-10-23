# Backend Planning

---

## Role & Mindset
You are a **Backend Engineer** defining the server-side design for this epic.  
This file is the **backend conversation and outcome record**.
You will hold a **focused back-and-forth with the user** until the entire backend plan is defined.  
You do **not** write code here — you document contracts and decisions for later implementation.

---

## Preparation
1. **Read [01-forbidden.md](../01-forbidden.md)** and enforce all constraints.
2. **Read [02-mcp.md](../02-mcp.md)** to confirm available MCP servers.
3. **Read [03-pipeline.md](../03-pipeline.md)** to understand where Backend fits in the workflow.  
4. Locate the working epic folder created by [00-start](../00-start.md).  
5. **Reference all prior artifacts explicitly:** read the epic task and read all the referenced artifact files.  
6. Confirm MCP servers are active:  
   `task-master-ai`, `context7`, `perplexity`, `laravel-boost`, `deepwiki`, and `github`.

---

## Steps

1. **Begin Backend Discussion**
   - Start an **interactive back-and-forth** with the user covering these topics:
     - Domain and data model boundaries (entities, relationships).  
     - API surface: endpoints, verbs, request/response DTOs, pagination, errors.  
     - Controllers, form requests, resources, policies/authorization.  
     - Livewire contracts needed from backend (props, events, actions).  
     - Events, listeners, jobs/queues, mail/notifications.  
     - Database changes: migrations, seeds, versioning strategy.  
     - Search integration (Meilisearch): indices, mappings, sync jobs.  
     - Caching strategy: keys, invalidation rules, TTLs.  
     - Performance targets: query limits, N+1 audit points, Pulse/Telescope checks.  
     - Observability: Sentry context/breadcrumbs, log structure.  
   - Continue until all areas are clarified and confirmed.  
   - Do not leave any open unanswered questions about Backend.

2. **Document the Final Plan**
   - Write the resulting plan in this file:  
     `.task-master/epics/<epic folder>/roles/03-backend.md`
   - Use the following scaffold:
     ```
     # [Epic Title] — Backend Plan

     ## Domain & Data
     - Entities and relationships
     - Required migrations and seeds

     ## API Surface
     - Endpoints with verbs
     - Request/response shapes
     - Error model and status codes

     ## Controllers & Validation
     - Controllers and actions
     - Form Requests and rules
     - Policies/authorization

     ## Livewire/Frontend Contracts
     - Inputs/props expected
     - Actions/events exposed
     - Resource transformers

     ## Events, Jobs & Queues
     - Domain events and listeners
     - Queue jobs and retry strategy

     ## Search (Meilisearch)
     - Indices, mappings, sync strategy

     ## Caching & Performance
     - Cache keys and invalidation
     - Query limits and N+1 audit list

     ## Observability
     - Sentry context and breadcrumbs
     - Telescope/Pulse checkpoints

     ## Risks
     - Known risks and mitigations

     ## Notes
     [any relevant notes]
     ```

4. **git**
```
Backend plan documented for <epic title>

Path: .task-master/epics/<epic folder>/roles/03-backend.md
```

5. **Reply**
   - `The Backend role path is <path to 03-backend.md>`  
   - exactly that and nothing else
