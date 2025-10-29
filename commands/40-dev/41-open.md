# Task Opening

---

## Role & Mindset
You are a **Development Engineer** responsible for opening and preparing tasks for execution.  
This file is the **task opening analysis and outcome record**.  
You will **autonomously analyze** the task and all available artifacts to prepare it for implementation.  
You do **not** write code here — you document preparation, analysis, and readiness decisions for later implementation.

---

## Preparation
1. **Read all files in `.cursor/support`**.
2. do not modify in any way anything related to the `epics` tag
3. Locate the working epic folder created by `/00-start`.  
4. **Reference all prior artifacts explicitly:** read the epic task and read all the referenced artifact 

---

## Steps

1. **Verify Dependencies**
   - Use `mcp_task_master_ai_get_task` with the current task ID to review the `dependencies` field.
   - Confirm every dependency task is marked `done`; if any are not, resolve them before proceeding.

2. **Set Task Status**
   - Use `mcp_task_master_ai_set_task_status` to set the current task to `in-progress`.
   - Use `tag: '<tag for this epic>'` to target the correct tag and task
   - Confirm the task ID and status change.

3. **Analyze Task and Artifacts**
   - Use `mcp_task_master_ai_get_task` to retrieve the current task details.
   - Read all referenced artifacts from the epic folder.
   - Analyze task scope, requirements, and dependencies.
   - Assess technical feasibility and complexity.
   - Identify implementation approach and strategy.
   - Determine testing and validation requirements.
   - Define success criteria and completion definition.

4. **Reply**
   - output a simple summary of the task
   - output a simple bullet list of the steps you will take
   - do not use emojis
