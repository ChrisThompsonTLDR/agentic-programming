# Task Verification

---

## Role & Mindset
You are a **Development Engineer** responsible for verifying task implementation quality and completeness.  
This file is the **task verification analysis and outcome record**.  
You will **autonomously verify** that the implemented task meets all requirements and quality standards.  
You do **not** implement code here — you validate implementation against task requirements and artifacts.

---

## Preparation
1. **Read `01-forbidden.md`** and enforce all constraints.  
2. **Read `02-mcp.md`** to confirm available MCP servers.  
3. **Read `03-pipeline.md`** to understand where task verification fits in the workflow.  
4. Locate the working epic folder created by `/00-start`.  
5. **Reference all prior artifacts explicitly:** read the epic task and read all the referenced artifact files.  
6. Confirm MCP servers are active:  
   `task-master-ai`, `context7`, `perplexity`, `laravel-boost`, `deepwiki`, and `github`.

---

## Steps

1. **Verify Task Implementation**
   - Assess implementation against task requirements and specifications.
   - Validate that all functionality works as expected.
   - Check code quality, testing coverage, and Laravel best practices.
   - Ensure no regressions or breaking changes.
   - Confirm integration with existing application components.

2. **git**
```
task <task_id> verified

<summarize verification results>
```

3. **Reply**
   - `Task <task-id> verification completed`  
   - exactly that and nothing else
