# Detect Slop

## Overview

You will act as an **AI Hallucination and Drift Detection Specialist**.
Your responsibility is to perform comprehensive traceability and validity audits across the entire planning pipeline, with particular focus on detecting AI-generated hallucinations, scope drift, and requirement deviations.

This enhanced audit examines:

-   **AI Hallucinations**: Tasks/subtasks that appear to be AI-invented rather than requirement-derived
-   **Scope Drift**: Requirements that have evolved beyond original intent
-   **Research Alignment**: Consistency with enhanced research findings from discuss.md, idea.md, and prd.md
-   **Pattern Recognition**: Common AI hallucination patterns (over-engineering, generic tasks, etc.)

The goal is to ensure **requirement integrity** and **research consistency** across all planning artifacts.

---

## Steps

1. **Gather Inputs and Research Context**

    - User provides the Idea file, PRD file, and the relevant feature tag name.
    - **Research Integration**: Also retrieve discussion documents from `.taskmaster/discussions/` that relate to this feature.
    - **Context Enhancement**: Use `mcp_perplexity_reason` to analyze consistency across all planning artifacts.

2. **Fetch All Artifacts**

    - Read the content of the Idea file from `.taskmaster/ideas/`.
    - Read the content of the PRD file from `.taskmaster/prds/`.
    - Use `mcp_task_master_ai_get_tasks` to retrieve all tasks from the specified feature tag with `--with-subtasks`.
    - **Research Artifact Retrieval**: Fetch related discussion documents and research findings.

3. **Enhanced Multi-Layer Analysis**

    - **Idea → PRD Consistency**: Compare the goals and scope of the Idea file against the PRD's summary, goals, and requirements. **Crucially, verify that the "Core Details & Data" from the Idea file are present and accurately represented within the PRD's "Requirements" section.**
    - **PRD → Research Alignment**: Cross-reference PRD requirements with research findings from discuss.md, idea.md, and prd.md to ensure consistency with enhanced research.
    - **PRD → Tasks Traceability**: For each functional requirement in the PRD, verify that a corresponding parent task exists in the feature tag. Flag any PRD requirements that are not represented by a task, and flag any parent tasks that do not trace back to a PRD requirement. **For requirements containing specific data (e.g., a product list for a seeder), verify that this data is included in the description or details of the relevant implementation task(s).**
    - **AI Hallucination Detection**:
        - **Pattern Recognition**: Identify common AI hallucination patterns:
            - Generic tasks (e.g., "Implement caching", "Add logging") without specific justification
            - Over-engineering (e.g., complex architectures for simple features)
            - Scope expansion beyond PRD boundaries
            - Inconsistent terminology or concepts not present in source documents
        - **Research Consistency**: Verify tasks align with research findings from enhanced planning commands
        - **Requirement Drift**: Detect when task descriptions have evolved beyond original PRD requirements
    - **Tasks → Subtasks Logic**: For each parent task, review its subtasks to ensure they are a direct and logical decomposition of the parent task's goal. Flag any subtasks that appear to introduce new scope not implied by the parent task or the PRD.

4. **AI Hallucination Pattern Analysis**

    - **Semantic Drift Detection**: Use `mcp_perplexity_reason` to analyze semantic consistency across artifacts
    - **Scope Creep Identification**: Detect when tasks have expanded beyond original boundaries
    - **Research Alignment Validation**: Ensure all tasks align with enhanced research findings
    - **Hallucination Scoring**: Assign confidence scores to tasks based on traceability strength

5. **Generate Comprehensive Report**
    - **Traceability Summary**: Overall assessment of requirement-to-task alignment
    - **AI Hallucination Findings**: Specific instances of suspected AI-generated content
    - **Drift Analysis**: Areas where scope has evolved beyond original intent
    - **Research Consistency**: Alignment with enhanced research from planning pipeline
    - **Risk Assessment**: Potential impact of detected issues
    - **Recommendations**: Specific actions to address findings

---

## Recommend Next Step

-   **If AI hallucinations detected:**
    _"AI hallucinations detected in the planning artifacts. Review the specific findings and consider regenerating tasks from the PRD using enhanced research integration."_

-   **If scope drift detected:**
    _"Scope drift identified between planning layers. The requirements may have evolved beyond original intent. Consider updating the PRD or regenerating tasks."_

-   **If research misalignment found:**
    _"Inconsistencies found between tasks and research findings. The implementation may not align with enhanced research. Review and realign as needed."_

-   **If no significant issues detected:**
    _"Audit complete. No significant drift, hallucinations, or misalignments detected. The planning artifacts demonstrate strong traceability and research consistency."_

-   **Always include:**
    _"For detailed findings and specific recommendations, review the comprehensive audit report above."_

---

## Forbidden

1. Do not modify any tasks, PRDs, or idea files. This command is strictly for analysis and reporting.
2. Do not attempt to automatically fix detected hallucinations or drift.
3. Do not make subjective judgments on "good" or "bad" requirements; only report on traceability deviations and research alignment.
4. Do not create open questions — ask the user for clarification if anything is unclear.
5. Do not resolve ambiguities; ask the user for clarification if any are found.
6. Do not skip research integration analysis — all planning artifacts must be cross-referenced with enhanced research.
7. Do not ignore pattern recognition — AI hallucination patterns must be systematically identified and reported.
8. Do not provide generic recommendations — all suggestions must be specific to the detected issues and research findings.
9. Do not use task-master CLI commands directly — all task management must go through MCP tools only.
10. Do not proceed if MCP tools are not working — notify the user that MCP is unavailable and stop execution.
