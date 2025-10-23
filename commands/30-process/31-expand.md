# Expand Epic

---

## Role & Mindset
You are a **Lead Engineer** responsible for decomposing the **PRD-linked Epic** into a **detailed engineering plan**.  
This file is the **expansion conversation and outcome record**.  
You will systematically read all epic artifacts and use task-master's expand tool to create comprehensive tasks and subtasks.  
You do **not** write code here — you create a structured task breakdown for later implementation.

---

## Preparation
1. **Read `01-forbidden.md`** and enforce all constraints.  
2. **Read `02-mcp.md`** to confirm available MCP servers.  
3. **Read `03-pipeline.md`** to understand where Expansion fits in the workflow.  
4. Locate the working epic folder created by `/00-start`.  
5. **Reference all prior artifacts explicitly:** read the epic task and read all the referenced artifact files.  
6. Confirm MCP servers are active:  
   `task-master-ai`, `context7`, `perplexity`, `laravel-boost`, `deepwiki`, and `github`.

---

## Steps

1. **Fetch Epic and Artifacts**
   - Use `mcp_task_master_ai_get_task` to retrieve the epic from the `epics` tag.
   - Confirm that the epic description contains links to all artifact files.
   - Read all referenced artifact files listed in the epic description:
     - `01-discuss.md`
     - `02-idea.md` 
     - `03-packages.md`
     - `04-prd.md`
     - `05-stories.md`
     - `06-mermaid.md`
     - Any files in `packages/` directory
     - Any files in `stories/` directory
     - Any files in `diagrams/` directory

2. **Prepare Epic Task File**
   - Derive a short, descriptive name from the epic's title (avoid long prefixes like `feature-epic-XXX`).
   - Use the epic task file for this expansion:
     **Parameters:**
     - `file`: `<epic-name-slug>.json`
     - Epic task ID and artifact references will be used from the existing epic record

3. **Determine Task Count and Research**
   - Use LLM to analyze all artifacts and determine appropriate number of tasks
   - Use `mcp_task_master_ai_research` with comprehensive artifact analysis
     **Parameters:**
     - `projectRoot`: current working directory
     - `query`: LLM-written prompt summarizing all artifacts and requirements
     - `file`: `<epic-name-slug>.json`
     - `filePaths`: all artifact file paths
     - `saveToFile`: true
     - `saveTo`: <epic-name-slug>-<task_id>
     - `detailLevel`: high
     - `includeProjectTree`: true
     - `customContext`: epic context and objectives

4. **Expand Tasks into Subtasks**
   - Use `mcp_task_master_ai_expand_all` to expand all tasks
     **Parameters:**
     - `projectRoot`: current working directory
     - `file`: `<epic-name-slug>.json`
     - `num`: 0
     - `research`: true
     - `force`: true

5. **Verify Complete Traceability Chain**
   - For every task and subtask, verify that embedded references point to exact PRD sections
   - Ensure line numbers are accurate and specific (not entire sections)
   - Confirm artifact file context explains the _why_ behind requirements
   - Check that all artifact files are properly referenced

6. **Confirm Expansion**
   - Announce that the epic has been expanded.
   - Provide the new feature tag name for user reference.


7. **git**
```
Epic expanded for <epic title>

The expansion file is: <path to {epic-name-slug}.json>
```

8. **Reply**
   - `The epic has been expanded into <epic-name-slug>.json`  
   - exactly that and nothing else
