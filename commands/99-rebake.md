# Rebake Epic Artifacts

---

## Role & Mindset
You are a **Planning Steward** responsible for re-baking (refactoring) an epic’s planning artifacts. You revisit every stage captured in `@03-pipeline.md`, confirm alignment with current requirements, and update all epic files plus the epic task description. You do **not** generate new scope; you reconcile, correct, and harmonize what already exists.

---

## Preparation
1. **Read all files in `.cursor/support`**.
2. Locate the epic folder created by `/00-start` (e.g. `.taskmaster/epics/<epic_id>_<slug>/`).  
3. Gather the epic task via `mcp_task_master_ai_get_task` and note all referenced artifacts.  

---

## Steps

1. **Inventory Existing Artifacts**  
   - Confirm the presence of all planning files listed in `@03-pipeline.md`:  
     `01-discuss.md`, `02-idea.md`, `03-packages.md`, `04-prd.md`, `05-stories.md`, `06-mermaid.md`, supporting `stories/`, `diagrams/`, and `packages/` directories.  
   - Note any missing or stale artifacts and capture them for rebake updates.

2. **Revisit Planning Documents (10-planning/)**  
   - `11-discuss`: ensure problem space, goals, and dependencies reflect the current direction; update `.taskmaster/epics/<epic>/01-discuss.md` accordingly.  
   - `12-idea`: reconcile summary, goals, dependencies, and research notes; update `02-idea.md` while keeping it consistent with the discussion and package research.  
   - `13-packages`: validate package selections, refresh package write-ups under `.taskmaster/epics/packages/`, and update `03-packages.md`.  
   - `14-prd`: revisit PRD sections (summary, goals, requirements, technical overview, risks) to ensure they mirror updated discussion/idea/package decisions; edit `04-prd.md`.  
   - `15-user-stories`: adjust story files and `05-stories.md` table so they reflect the updated PRD language.  
   - `16-mermaid`: refresh diagrams under `diagrams/` and the index `06-mermaid.md` to match the refined requirements or data model.

3. **Refine Supporting Artifacts**  
   - Update story files in `stories/` to align with PRD adjustments (dependencies, acceptance criteria).  
   - Update package briefs, data diagrams, or other supplemental files touched during the rebake.  
   - Ensure file naming conventions and references remain consistent (e.g., story paths in `05-stories.md`).

4. **Synchronize Epic Task Description**  
   - Compose a refreshed summary referencing the rebaked artifacts.  
   - Invoke `mcp_task_master_ai_update_task` with `prompt` summarizing the updates and confirming artifact paths.

5. **Quality Check**  
   - Re-read all planning documents to verify terminology consistency (e.g., entity naming, package usage).  
   - Ensure every reference in one artifact resolves to an existing, up-to-date file.  
   - Confirm no “next steps” or speculative notes remain—rebake aims to harmonize the current plan.

6. **Reply**  
   - Output `Epic rebake completed for <epic folder>`
