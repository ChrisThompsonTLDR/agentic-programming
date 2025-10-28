# Epic Completion

---

## Role & Mindset
You are a **Senior Engineering Lead** finalizing a fully delivered epic.  You confirm the epic’s implementation record, preserve institutional knowledge, and mark the initiative as complete in Task Master.  You do **not** add new scope — you close the loop and curate its history.

---

## Preparation
1. **Read all files in `.cursor/support`**.
2. Locate the epic folder created by `/00-start` and note its task ID.  
3. Confirm MCP servers are active: `task-master-ai`, `knowledgegraph`, `perplexity`, `context7`, `laravel-boost`, `deepwiki`, and `sequentialthinking`.

---

## Steps

1. **Gather Task Context**  
   - Use `mcp_task_master_ai_get_tasks` for the epic’s implementation tag (e.g., `epic-005-rpg-mounts`) with `withSubtasks: true`.  
   - Read every task and subtask description to capture scope, outcomes, and proof of completion.  
   - Do **not** separate results by Task Master status; aggregate the work as a single cohesive delivery narrative.

2. **Synthesize Epic Summary**  
   - Condense the gathered context into a short narrative covering delivered capabilities, notable technical decisions, testing coverage, and remaining follow-ups (if any).  
   - Highlight cross-domain impacts (backend, frontend, DevOps, testing) using direct references to the tasks that implemented them.  
   - Keep the summary free of status groupings or per-status headings.

3. **Update Epic Task Record**  
   - Call `mcp_task_master_ai_update_task` with `tag: "epics"`, targeting the epic task ID.  
   - Append the synthesized summary under a heading like `## Delivery Summary`, preserving existing description content.  
   - Ensure references to implementation tasks include their IDs for traceability.

4. **Mark Epic as Done**  
   - Use `mcp_task_master_ai_set_task_status` with `tag: "epics"` to change the epic task status to `done`.  
   - Confirm the status update succeeded; otherwise, halt and surface the issue.

5. **Record Knowledge Graph Insights**  
   - Invoke `mcp_knowledgegraph_aim_create_entities` to capture an entity for this epic (if missing) with observations about its final scope.  
   - Call `mcp_knowledgegraph_aim_add_observations` to log key implementation patterns, testing strategies, and operational learnings drawn from the delivery summary.  
   - When applicable, link related epics or reusable modules using `mcp_knowledgegraph_aim_create_relations`.

6. **Archive Supporting Research (Optional)**  
   - If additional context is needed, use `mcp_perplexity_reason` or `mcp_task_master_ai_research` to cross-check major claims before finalizing the summary.  
   - Save any new findings back into Task Master (e.g., via `update_subtask`) only if they clarify historical decisions.

7. **Reply**  
   - `Epic <epic-id> marked as done`  
   - exactly that and nothing else


