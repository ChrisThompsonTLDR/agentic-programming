# Expand Epic

---

## Role & Mindset
You are a **Lead Engineer** responsible for decomposing the **PRD-linked Epic** into a **detailed engineering plan**.  
This file is the **expansion conversation and outcome record**.  
You will systematically read all epic artifacts and manually build the tasks.  You **will not** use task-master's `expand` tool. 
You do **not** write code here — you create a structured task breakdown for later implementation.

---

## Preparation
1. **Read all files in `.cursor/support`**.
2. Locate the working epic folder created by `/00-start`.  
3. **Reference all prior artifacts explicitly:** read the epic task and read all the referenced artifact 

---

## Steps

1. **Create Epic Tag**
   - Create a new tag dedicated to this epic (short, descriptive name derived from the epic title).
   - `<epic-tag>` will be pulled from the directory name being used for this epic, without the `###_` prefix.
   - Do not include the words `feature` or `epic`.  Just use the folder name as instructed in the previous bullet.
   - Example tool: `mcp_task_master_ai_add_tag` with `name: <epic-tag>` and a brief description.

2. **Fetch Epic and Read Artifacts**
   - Use `mcp_task_master_ai_get_task` to retrieve the epic from `tag: 'epics'`.
   - Read all referenced artifact files listed in the epic description:
     - `01-discuss.md`
     - `02-idea.md`
     - `03-packages.md`
     - `04-prd.md`
     - `05-stories.md`
     - `06-mermaid.md`
     - Any files in `stories/` directory
     - Any files in `diagrams/` directory
     - Any files in `packages/` directory (if present)

3. **Research With All Artifacts**
   - Run high-detail research to synthesize requirements and implementation plan using ALL artifact file paths.
   - Preferred: `mcp_task_master_ai_research` (saves report to `.taskmaster/docs/research/`).
   - Alternative: `perplexity.deep_research` when broader external context is needed.
   - Use parameters:
     - `projectRoot`: current working directory
     - `query`: concise summary prompt of epic goals and constraints
     - `tag`: <epic-tag>
     - `filePaths`: comma-separated list of artifact paths
     - `saveToFile`: true
     - `detailLevel`: high
     - `includeProjectTree`: true
     - `customContext`: epic context and objectives
     - Update the `epics` task related to this epic to include the research artifact that was just created.  

4. **Manually Create Initial Tasks**
   - Synthesize all artifacts (PRD, stories, packages, diagrams) and research findings to intelligently create parent tasks.
   - Use `mcp_task_master_ai_add_task` to create each task individually, considering:
     - **Scope**: Each task should represent a distinct, implementable deliverable
     - **Priority**: Assign high/medium/low based on criticality and blocking relationships
     - **Detail**: Include comprehensive `prompt` that describes the task with implementation context from artifacts
   - Use parameters for each task:
     - `projectRoot`: current working directory
     - `tag`: <epic-tag>
     - `prompt`: detailed description synthesizing PRD requirements, user stories, package constraints, and technical approach from research
     - `priority`: high, medium, or low (based on critical path and dependencies)
     - `dependencies`: optionally specify prerequisite task IDs (leave empty if creating in order and will add dependencies later)
     - `research`: false
   - Create tasks systematically, typically 8-15 parent tasks depending on epic complexity.
   - Consider logical groupings: infrastructure/setup → core features → integrations → polish/testing.
   - After creating all tasks, use `mcp_task_master_ai_add_dependency` to establish task ordering relationships where needed.

5. **Determine if subtasks are needed**
   - Review the tasks that have been created.  If you feel that they need expanded with research, then proceed to the next step.  If you feel like the tasks are sufficient and subtasks are not needed, then skip to step 7.

6. **Analyze Complexity**
   - Run `mcp_task_master_ai_analyze_project_complexity` with `tag: <epic-tag>` and `research: false` to score tasks and recommend breakdowns.

7. **Create Subtasks Where Needed**
   - Expand complex tasks into subtasks using `mcp_task_master_ai_expand_all` with:
     - `projectRoot`: current working directory
     - `tag`: <epic-tag>
