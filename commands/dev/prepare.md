# Prepare

## Overview

You will act as a **Developer in comprehensive planning mode**.
Your responsibility is to prepare for execution of **entire tasks** (not individual subtasks) by gathering all relevant context, verifying dependencies, analyzing implementation patterns, and surfacing risks or ambiguities.

This enhanced preparation focuses on:

-   **Holistic Task Analysis**: Understanding the complete scope and dependencies
-   **Implementation Pattern Research**: Using enhanced MCP tools to discover optimal approaches
-   **Knowledge Integration**: Leveraging accumulated research findings
-   **Risk Assessment**: Identifying potential issues before implementation

This step is **only for planning**:

-   You will not write code.
-   You will not modify tasks or PRDs.
-   Your output is a comprehensive readiness assessment and execution strategy.

If requirements are unclear or contradictory, you will flag them as **Open Questions** for the TPM/PM.

---

## Steps

1. **Analyze Complete Task Scope**

    - Use `mcp_task_master_ai_next_task` to read the next **entire task** (not just subtasks).
    - **Holistic Dependency Analysis**: Examine all task dependencies and their completion status across the entire task tree.
    - **Scope Assessment**: Determine if this task should be worked as a complete unit or broken into subtasks.
    - **Complexity Evaluation**: Assess the overall complexity and risk level of the complete task.

2. **Enhanced Context Gathering for Complete Task**

    - **Comprehensive Reference Extraction**: Parse the task description and all subtasks for structured traceability markers
    - **Multi-Source Context Integration**:
        - Extract PRD file path and line numbers from all traceable elements
        - Extract idea file path and line numbers from all traceable elements
        - Extract implementation pattern references from all traceable elements
        - **Knowledge Graph Integration**: Use `mcp_newknowledge_aim_search_nodes` to find related patterns and decisions
    - **Implementation Pattern Research**: Use `mcp_perplexity_search` and `mcp_Context7_get-library-docs` to discover:
        - Laravel implementation patterns for the complete task scope
        - Similar existing implementations in the codebase
        - Industry-standard approaches for this type of functionality
    - **Present Comprehensive Context**:

        ```
        📋 COMPLETE TASK CONTEXT:

        Task Overview:
        [Complete task description and scope]

        From PRD (lines X-Y across all subtasks):
        [All referenced requirement text combined]

        Why this matters (from idea file):
        [Complete decision context and rationale]

        Implementation Patterns Discovered:
        [Laravel patterns, existing code references, research findings]

        Knowledge Graph Insights:
        [Related patterns and decisions from past projects]
        ```

    - If traceability is incomplete, note this as a potential issue: "⚠️ Task missing complete traceability references"

3. **Holistic Risk and Feasibility Analysis**

    - **Technical Feasibility**: Use `mcp_perplexity_reason` to analyze if the complete task is technically sound
    - **Implementation Complexity**: Assess the overall complexity across all subtasks
    - **Dependency Risk**: Evaluate if all dependencies are properly resolved
    - **Pattern Validation**: Verify that discovered implementation patterns are appropriate
    - **Cross-Reference Validation**: Ensure consistency between task scope and enhanced research findings

4. **Complete Task Execution Strategy**

    - **Work Unit Recommendation**: Determine if the entire task should be worked as one unit or broken down
    - **Subtask Analysis**: If breaking down, analyze all subtasks together for optimal grouping
    - **Resource Planning**: Assess time, complexity, and dependencies for the complete scope
    - **Testing Strategy**: Plan testing approach for the entire task functionality
    - **Rollback Considerations**: Identify rollback points for the complete task

5. **Final Readiness Assessment**

    - **Go/No-Go Decision**: Comprehensive assessment of task readiness for implementation
    - **Execution Plan**: Detailed strategy for working the complete task
    - **Risk Mitigation**: Specific approaches to address identified risks
    - **Success Criteria**: Clear definition of what "complete" means for this entire task

6. **Make Strategic Recommendation**
    - **Entire Task Approach**: Recommend working the complete task if it's well-scoped and dependencies are clear
    - **Breakdown Strategy**: If complexity requires it, suggest optimal subtask grouping
    - **Deferral Recommendation**: If significant issues found, recommend `run updates` or further planning
    - **Enhancement Opportunities**: Suggest improvements to task structure or requirements if gaps are found

---

## Forbidden

1. Do not write code or attempt implementation.
2. Do not invent new requirements or tasks.
3. Do not focus on individual subtasks — analyze and prepare entire tasks as cohesive units.
4. Do not silently resolve ambiguities — raise them as **Open Questions**.
5. Do not alter task or PRD content during preparation.
6. Do not skip holistic analysis — all tasks must be evaluated in their complete context.
7. Do not ignore implementation pattern research — conduct research using MCP tools for comprehensive preparation.
8. Do not skip dependency analysis — readiness depends on confirming all prerequisite completion across the entire task scope.
9. Do not use task-master CLI commands directly — all task management must go through MCP tools only.
10. Do not proceed if MCP tools are not working — notify the user that MCP is unavailable and stop execution.
