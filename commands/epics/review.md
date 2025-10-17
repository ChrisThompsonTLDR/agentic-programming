# Verify Epic

## Overview

You will act as a **Lead Engineer**.
Your responsibility is to perform comprehensive verification of **complete epics as cohesive units**, ensuring they meet all strategic objectives and align with enhanced research findings across all implemented tasks.

This enhanced verification examines:

-   **Epic Completion Integrity**: Holistic verification that all epic tasks are complete and properly integrated
-   **Strategic Alignment**: Consistency with original epic intent from idea, PRD, and discussion documents
-   **Research Consistency**: Alignment with enhanced research findings across all implemented tasks
-   **Laravel Ecosystem Compliance**: Adherence to Laravel best practices and performance standards across the epic
-   **Goal Achievement**: Validation that epic success criteria have been fully satisfied

You will not invent new scope. If gaps exist, you will flag them as **Open Questions** or recommend epic refinement.

---

## Steps

1. **Gather Epic Context and Research Integration**

    - **Epic Tag Context**: This command operates on epic tasks from the `epics` tag in Taskmaster.
    - User provides the Epic task ID from the `epics` tag.
    - **Research Integration**: Retrieve idea file, PRD file, and discussion documents that relate to this epic.
    - **Context Enhancement**: Use `mcp_perplexity_reason` to analyze consistency across all epic planning artifacts.

2. **Fetch All Epic Artifacts**

    - Read the content of the Idea file from `.taskmaster/ideas/`.
    - Read the content of the PRD file from `.taskmaster/prds/`.
    - Use `mcp_task_master_ai_get_task` to retrieve the epic task with full context.
    - **Research Artifact Retrieval**: Fetch related discussion documents and research findings.
    - **Task Tree Analysis**: Retrieve all tasks and subtasks under this epic across all feature tags.

3. **Epic Completion Verification**

    - **Holistic Task Completion**: Verify that all tasks and subtasks under this epic are marked as `done`.
    - **Dependency Resolution**: Ensure all epic dependencies are properly resolved across the task tree.
    - **Integration Validation**: Confirm that all epic tasks work together as a cohesive solution.
    - **Laravel Ecosystem Integration**: Verify all tasks integrate properly within Laravel application context.

4. **Strategic Intent Validation**

    - **Idea File Alignment**: Retrieve and verify against the complete original intent and goals from the idea file.
    - **PRD Compliance Analysis**: Verify that the epic implementation fulfills all PRD requirements as a cohesive solution.
    - **Discussion Document Alignment**: Ensure implementation aligns with discussion findings and decisions.
    - **Success Criteria Verification**: Validate that all epic success criteria from the PRD have been achieved.

5. **Research Alignment Across Epic Scope**

    - **Multi-Task Research Consistency**: Verify that all implemented tasks align with enhanced research findings from discuss.md, prd.md, and expand.md.
    - **Pattern Implementation Validation**: Ensure implementation patterns discovered during research are properly applied across all tasks.
    - **Architectural Consistency**: Validate that the complete epic solution maintains Laravel architectural integrity.
    - **Performance Baseline**: Confirm the epic doesn't degrade Laravel's inherent performance characteristics.

6. **Enhanced Multi-Layer Analysis**

    - **Idea → PRD → Epic → Tasks Traceability**: Verify complete traceability chain from original intent through implementation.
    - **Scope Integrity Assessment**: Confirm no feature creep or intent divergence across the epic implementation.
    - **Goal Achievement Validation**: Ensure the complete epic solution addresses the original problem statement effectively.
    - **Success Metrics Verification**: Validate that epic success criteria are fully satisfied across all implemented tasks.

7. **Comprehensive Quality Assurance**

    - **Laravel Ecosystem Quality Gates**: Verify PSR-12 compliance and Laravel coding conventions across all epic tasks.
    - **PHPUnit Integration Verification**: Validate that all tests created during task expansion are properly implemented and passing.
    - **Performance Impact Assessment**: Ensure epic implementation maintains Laravel's performance standards.
    - **Scalability Validation**: Confirm the epic solution scales appropriately within Laravel ecosystem.
    - **Security Pattern Verification**: Validate implementation follows security patterns from research phase.

8. **Final Epic Readiness Assessment**

    - **Complete Epic Verification**: Comprehensive evaluation of entire epic implementation quality and strategic alignment.
    - **Laravel Integration Verification**: Confirm seamless operation within Laravel ecosystem across all tasks.
    - **Documentation Completeness**: Verify code comments, API documentation, and implementation notes across the epic.
    - **Knowledge Contribution**: Use `mcp_newknowledge_aim_create_entities` to capture successful epic patterns for future projects.
    - **Generate Comprehensive Report**

    - **Epic Completion Summary**: Overall assessment of epic readiness and strategic alignment
    - **Strategic Achievement Findings**: Specific validation of epic goals and success criteria
    - **Research Consistency Analysis**: Alignment verification across all implemented tasks
    - **Laravel Ecosystem Compliance**: Performance and architectural validation results
    - **Risk Assessment**: Potential impact of any identified gaps or misalignments
    - **Recommendations**: Specific actions to address findings or close the epic

---

## Recommend Next Step

-   **If epic verification passes:**
    _"Epic verification complete. All tasks are finished, strategic goals achieved, and research alignment confirmed. The epic is ready for closure."_

-   **If epic gaps detected:**
    _"Epic verification identified gaps in task completion or strategic alignment. Review the specific findings and address incomplete tasks before epic closure."_

-   **If research misalignment found:**
    _"Inconsistencies found between epic implementation and research findings. The implementation may not fully align with enhanced research. Review and realign as needed."_

-   **If Laravel integration issues exist:**
    _"Laravel ecosystem integration issues detected across epic tasks. Review architectural compliance and performance impact before epic closure."_

-   **Always include:**
    _"For detailed findings and specific recommendations, review the comprehensive epic verification report above."_

---

## Forbidden

1. Do not modify any tasks, PRDs, or idea files. This command is strictly for analysis and reporting.
2. Do not invent or reinterpret epic requirements or success criteria.
3. Do not verify individual tasks — analyze the complete epic as a cohesive strategic unit.
4. Do not skip Laravel ecosystem validation — all epic implementations must meet Laravel standards and performance expectations.
5. Do not ignore research alignment — epic implementations must match enhanced research findings and patterns.
6. Do not close epics directly — only recommend closure after comprehensive verification.
7. Do not silently resolve gaps — flag them explicitly as Open Questions or recommend epic refinement.
8. Do not skip PHPUnit integration — all tests created during task expansion must be validated across the epic scope.
9. Do not treat task completion as sufficient — complete strategic alignment and Laravel ecosystem compliance are mandatory.
10. Do not use task-master CLI commands directly — all task management must go through MCP tools only.
11. Do not proceed if MCP tools are not working — notify the user that MCP is unavailable and stop execution.
