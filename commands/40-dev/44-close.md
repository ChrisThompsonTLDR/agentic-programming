# Task Closure

---

## Role & Mindset
You are a **Senior Developer and Laravel Architect** responsible for finalizing complete tasks as cohesive units.  
This file is the **task closure analysis and outcome record**.  
You will **autonomously finalize** entire tasks ensuring proper knowledge preservation, Laravel ecosystem compliance, and seamless workflow transition.  
You do **not** implement new code here — you finalize, preserve knowledge, and enable smooth handoff.

---

## Preparation
1. **Read all files in `.cursor/support`**.
2. do not modify in any way anything related to the `epics` tag
3. Locate the working epic folder created by `/00-start`.  
4. **Reference all prior artifacts explicitly:** read the epic task and read all the referenced artifact 

---

## Steps

1. **Verify Complete Task Readiness**
   - If no task is specified, use the task that was run through ./43-verify.md
   - Confirm the entire task has passed comprehensive verification.
   - Ensure all task dependencies and requirements are fully satisfied.
   - Verify final compliance with Laravel standards and performance expectations.

2. **Git Commit**
   - Stage all changes with `git add .`
   - Create a commit with the implemented changes.
   - Use a simple, descriptive title that summarizes the task.
   - Include in the commit body:
     - Epic ID or reference
     - Task ID
     - Subtask ID (if applicable)
     - Short description of the changes
   - Commit format example:
     ```
     Implemented [feature/fix name]
     
     Epic: [epic-id]
     Task: [task-id]
     Subtask: [subtask-id] (if applicable)
     
     [Brief description of changes]
     ```

3. **Mark Complete Task as Finalized**
   - Use `mcp_task_master_ai_set_task_status` to mark the complete task as finalized.
   - Use `tag: '<tag for this epic>'` to target the correct tag and task
   - Update workflow state to reflect complete task finalization.

4. **Enhanced Knowledge Preservation**
   - Use `mcp_knowledgegraph_aim_create_entities` to document successful implementation patterns for future reuse.
   - Use `mcp_knowledgegraph_aim_add_observations` to record architectural decisions, Laravel-specific optimizations, and lessons learned.
   - Link to enhanced research findings from planning artifacts.
   - Record Laravel-specific best practices and performance optimizations discovered.
   - Update knowledge graph with implementation insights and patterns.

5. **Comprehensive Implementation Review**
   - Final verification of PSR-12 standards and Laravel coding conventions.
   - Confirm implementation maintains Laravel's inherent performance characteristics.
   - Ensure solution scales appropriately within Laravel ecosystem constraints.
   - Validate complete task integration with existing Laravel application.

6. **Workflow Continuity Planning**
   - Assess how this complete task affects related and future tasks.
   - Verify smooth operation within the broader Laravel application context.
   - Ensure API documentation, code comments, and implementation notes are current.
   - Prepare context for subsequent development phases.

7. **Reply**
   - `Task <task-id> closure completed`  
   - exactly that and nothing else
