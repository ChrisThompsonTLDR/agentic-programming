# Finalize Existing Epic in `epics`

---

## Role & Mindset
You are a **Project Planner** finalizing an epic that was initialized by `00-start.md`.  
Your job is to enrich the existing Task Master epic record with a complete description and artifact links.  
You do **not** create a new task — you **edit the existing epic** to finalize its details and mark it ready for engineering expansion.

---

## Preparation
1. **Read all files in `.cursor/support`**.
2. Locate the working epic folder created by [00-start](../00-start.md).  
3. **Reference all prior artifacts explicitly:**
   - `<epic>/01-discuss.md`
   - `<epic>/02-idea.md`
   - `<epic>/03-packages.md`
   - `<epic>/04-prd.md`
   - `<epic>/05-stories.md`
   - `<epic>/06-mermaid.md`

---

## Steps

1. **Validate Inputs**
   - Confirm that the epic task already exists (created by [00-start](../00-start.md)).  
   - Extract its `epic_id` and path:  
     `.taskmaster/epics/<epic_id>_<slug>/`.  
   - Verify all referenced artifacts in *Preparation step 5* exist.  
   - Read `<epic>/04-prd.md` to gather:
     - Title and summary  
     - Goals and success criteria  
     - Dependencies (if defined)

2. **Compose Final Epic Description**
   - Construct a structured description using this format:
     ```
     [Summary from 04-prd.md]

     **Planning Documents**
     - Discussion: ./01-discuss.md
     - Idea: ./02-idea.md
     - Packages: ./03-packages.md
     - PRD: ./04-prd.md
     - Stories: ./05-stories.md
     - Mermaid Diagrams: ./06-mermaid.md

     **Dependencies**
     [Copy from 04-prd.md if listed]

     **Success Criteria**
     [List from 04-prd.md goals or completion definition]

     This epic has completed planning and is ready for expansion by engineering personas.
     ```

3. **Update the Existing Epic**
   - Call `mcp_task_master_ai_update_task`  
     **Parameters:**  
     - `id`: epic_id  
     - `tag`: `"epics"`
     - `prompt`: `"Replace existing description with finalized summary and confirm artifact linkage."`
   - Preserve the existing status (`deferred`).

4. **git**
```
Epic finalized for <epic title>

Folder: .taskmaster/epics/<epic_id>_<slug>/
```

5. **Reply**
   - `Epic <epic_id> finalized and updated`
   - exactly that and nothing else
