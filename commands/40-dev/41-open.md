# Task Opening

---

## Role & Mindset
You are a **Development Engineer** responsible for opening and preparing tasks for execution.  
This file is the **task opening analysis and outcome record**.  
You will **autonomously analyze** the task and all available artifacts to prepare it for implementation.  
You do **not** write code here — you document preparation, analysis, and readiness decisions for later implementation.

---

## Preparation
1. **Read `01-forbidden.md`** and enforce all constraints.  
2. **Read `02-mcp.md`** to confirm available MCP servers.  
3. **Read `03-pipeline.md`** to understand where task opening fits in the workflow.  
4. Locate the working epic folder created by `/00-start`.  
5. **Reference all prior artifa# Task Opening

---

## Role & Mindset
You are a **Development Engineer** responsible for opening and preparing tasks for execution.  
This file is the **task opening analysis and outcome record**.  
You will **autonomously analyze** the task and all available artifacts to prepare it for implementation.  
You do **not** write code here — you document preparation, analysis, and readiness decisions for later implementation.

---

## Preparation
1. **Read all files in `.cursor/support`**.
2. Locate the working epic folder created by `/00-start`.  
3. **Reference all prior artifacts explicitly:** read the epic task and read all the referenced artifact files.  
4. Confirm MCP servers are active:  
   `task-master-ai`, `context7`, `perplexity`, `laravel-boost`, `deepwiki`, and `github`.

---

## Steps

1. **Set Task Status**
   - Use `mcp_task_master_ai_set_task_status` to set the current task to `in-progress`.
   - Use `tag: 'epics'` to target tasks in the epics tag.
   - Confirm the task ID and status change.

2. **Analyze Task and Artifacts**
   - Use `mcp_task_master_ai_get_task` to retrieve the current task details.
   - Read all referenced artifacts from the epic folder.
   - Analyze task scope, requirements, and dependencies.
   - Assess technical feasibility and complexity.
   - Identify implementation approach and strategy.
   - Determine testing and validation requirements.
   - Define success criteria and completion definition.

3. **Reply**
   - output a simple summary of the task
   - output a simple bullet list of the steps you will take
   - do not use emojis
cts explicitly:** read the epic task and read all the referenced artifact files.  
6. Confirm MCP servers are active:  
   `task-master-ai`, `context7`, `perplexity`, `laravel-boost`, `deepwiki`, and `github`.

---

## Steps

1. **Set Task Status**
   - Use `mcp_task_master_ai_set_task_status` to set the current task to `in-progress`.
   - Confirm the task ID and status change.

2. **Analyze Task and Artifacts**
   - Use `mcp_task_master_ai_get_task` to retrieve the current task details.
   - Read all referenced artifacts from the epic folder.
   - Analyze task scope, requirements, and dependencies.
   - Assess technical feasibility and complexity.
   - Identify implementation approach and strategy.
   - Determine testing and validation requirements.
   - Define success criteria and completion definition.

3. **git**
```
task <task_id> in-progress

task <task_id> is now in progress
```

4. **Reply**
   - `Task <task-id> opened and ready for implementation`  
   - exactly that and nothing else
