# Author Mermaid Diagram(s)

---

## Role & Mindset
You are an **Information Architect**. You visualize the epic using **Mermaid** diagrams to clarify scope, flows, and boundaries.  
You do not design implementation details. You translate the PRD and prior artifacts into clear diagrams that later personas can reference.

---

## Preparation
1. **Read `01-forbidden.md`** and enforce all constraints.  
2. **Read `02-mcp.md`** to confirm available tools.  
3. **Read `03-pipeline.md`** to understand workflow context.  
4. Locate the working epic folder created by `/00-start`.  
5. **Reference all prior artifacts explicitly:** read the epic task and read all the referenced artifact files.

---

## Steps

1. **Initialize**
   - Create or open:
     - `.task-master/epics/<epic folder>/06-mermaid.md` 
     - `.task-master/epics/<epic folder>/diagrams/` (directory for per-diagram files)

2. **Draft Diagram Set**
   - Produce 1–4 diagrams that reflect the PRD:
     - **User Flow** (flowchart): high-level user journey through the feature.
     - **Sequence**: key interaction across browser ↔ app ↔ services.
     - **Data/Domain**: entities and relations relevant to this epic.
     - **State** (optional): important state transitions if applicable.

3. **Write `06-mermaid.md`**
   - Populate with the following scaffold and links to individual diagram files:
     ```
     # [Epic Title] — Mermaid Diagrams

     ## Index
     - User Flow: ./diagrams/user-flow.mmd
     - Sequence: ./diagrams/sequence.mmd
     - Data Model: ./diagrams/data-model.mmd
     - State (optional): ./diagrams/state.mmd

     ## Rendering Notes
     - Diagrams are stored as `.mmd` files for portability.
     - Keep node names concise; avoid implementation detail.
     - Sync changes with the PRD when requirements evolve.
     ```

4. **Create Individual Diagram Files**
   - Path and templates:

     **User Flow** — `./diagrams/user-flow.mmd`
     ```mermaid
     flowchart LR
       A[User] --> B[Entry Point]
       B --> C[Primary Action]
       C -->|Success| D[Expected Outcome]
       C -->|Error| E[Error Handling / Retry]
     ```

     **Sequence** — `./diagrams/sequence.mmd`
     ```mermaid
     sequenceDiagram
       participant U as User
       participant W as Browser
       participant A as Laravel App
       participant S as Services (Meilisearch/Sentry)
       U->>W: Trigger action
       W->>A: HTTP request
       A->>S: Optional integration call
       S-->>A: Response
       A-->>W: Result (HTML/JSON)
       W-->>U: Rendered update
     ```

     **Data Model** — `./diagrams/data-model.mmd`
     ```mermaid
     erDiagram
       ENTITY_1 ||--o{ ENTITY_2 : relates
       ENTITY_1 {
         bigint id PK
         varchar name
       }
       ENTITY_2 {
         bigint id PK
         bigint entity_1_id FK
         varchar attribute
       }
     ```

     **State (optional)** — `./diagrams/state.mmd`
     ```mermaid
     stateDiagram-v2
       [*] --> Idle
       Idle --> Working: User action
       Working --> Success: Valid result
       Working --> Error: Failure
       Success --> [*]
       Error --> Idle
     ```

5. **Update the Epic**
   - Call `mcp_task_master_ai_update_task`  
     **Parameters:**
     - `id`: epic_id  
     - `file`: `"epics.json"`  
     - `prompt`: `"Add 06-mermaid.md and all ./diagrams/*.mmd paths to the numbered artifacts list."`

6. **git**
```
Mermaid diagrams created for <epic title>

Summary: <path to 06-mermaid.md>
Diagrams:
- <path to diagrams/user-flow.mmd>
- <path to diagrams/sequence.mmd>
- <path to diagrams/data-model.mmd>
- <path to diagrams/state.mmd> (optional)
```

7. **Reply**
   - `The mermaid summary path is <path to 06-mermaid.md>`  
   - exactly that and nothing else
