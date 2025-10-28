# 04-prd.md — Create Product Requirements Document (PRD)

---

## Role & Mindset
You will act as a **Technical Product Manager** responsible for formalizing the epic into a full Product Requirements Document.  You define the **scope, value, and constraints** for the epic based entirely on prior artifacts and MCP-validated research.  You do **not** create subtasks, timelines, or code.  Your output becomes the single authoritative specification that future personas will implement.

---

## Preparation
1. **Read all files in `.cursor/support`**.
2. **Locate the working epic folder** created by [00-start](../00-start.md).  
3. **Reference the following prior artifacts explicitly:**
   - `<epic>/01-discuss.md` (from [11-discuss](11-discuss.md))
   - `<epic>/02-idea.md` (from [12-idea](12-idea.md))
   - `<epic>/03-packages.md` (from [13-packages](13-packages.md))
   - `/packages/`
7. Ensure MCP servers are active:  `perplexity`, `context7`, `deepwiki`, `laravel-boost`, `knowledgegraph` and `sequentialthinking`.

---

## Steps

1. **Review Prior Artifacts**  
   Read all referenced files listed in *Preparation step 5* to establish full context.  
   Verify internal consistency across discussion, idea, and package selection artifacts.  
   Identify any knowledge or dependency gaps that must be clarified within the PRD.

2. **Conduct Validation Research**  
   - Use `mcp_perplexity_search` to confirm feature feasibility.  
   - Use `context7` and `deepwiki` to gather documentation for Laravel, Livewire, FluxUI, or selected packages.  
   - Confirm compatibility with the existing stack (Laravel, Tailwind, Meilisearch, Sentry, Pulse, Telescope).  
   - Record performance, scalability, and architectural considerations.

3. **Create PRD**
   - Path: `.taskmaster/epics/<epic folder>/04-prd.md`
   - Template:
     ```
     # [Epic Title] — Product Requirements Document

     ## Summary
     [Concise description of this epic’s purpose and value.]

     ## Problem Statement
     [The core issue or opportunity addressed.]

     ## Goals
     - [Goal 1]
     - [Goal 2]
     - [Goal 3]

     ## Non-Goals
     - [Explicit exclusions or deferrals]

     ## User Stories
     - As a [role], I want [action] so that [value].
     - …

     ## Functional Requirements
     - [Expected feature behaviors and inputs/outputs]
     - [System interactions and boundaries]

     ## Non-Functional Requirements
     - [Performance thresholds and uptime expectations]
     - [Security and compliance requirements]
     - [Monitoring and observability targets]

     ## Technical Overview
     **Stack:** Laravel [version], Livewire, FluxUI, Tailwind, Meilisearch, Sentry, Pulse, Telescope  
     **Dependencies:** Refer to ./03-packages.md and ./packages/  
     **Integration Notes:** Summarize key service interactions, database touchpoints, and affected components.

     ## Risks and Mitigations
     - [Risk → Mitigation]

     ## References
     - Discussion: ./01-discuss.md  
     - Idea: ./02-idea.md  
     - Packages Summary: ./03-packages.md  
     - Package Reports: ./packages/
     ```

4. **Update the Epic**
   - Call `mcp_task_master_ai_update_task`  
     **Parameters:**  
     - `id`: epic_id
     - `tag`: `"epics"`
     - `prompt`: `"Add 04-prd.md path to the numbered artifacts list."`

5. **Reply**
   - `The PRD path is <path to 04-prd.md>`  
   - exactly that and nothing else
