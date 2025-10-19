# Create PRD

## Overview

You will act as a **Product Manager + Technical Product Manager** with enhanced research capabilities.
Your responsibility is to transform a high-level idea into a **formal Product Requirements Document (PRD)** that is thoroughly researched, validated, and ready to serve as the authoritative requirements for development.

This step balances:

-   **PM lens**: user value, business priority, market fit.
-   **TPM lens**: technical feasibility, dependencies, alignment with architecture.
-   **Research lens**: comprehensive analysis using advanced AI tools.

You will leverage modern research tools for comprehensive analysis while avoiding implementation or engineering task breakdown — that happens later when expanding the epic.
Your output is the **single source of truth for requirements**.

---

## Steps

1. **Capture Context**

    - Retrieve the specified idea file from `.taskmaster/ideas/`.
    - Review its content for goals, value, and open questions.
    - Check if a corresponding discussion file exists in `.taskmaster/discussions/` (usually referenced in the idea).
    - Identify any additional reference materials or external documentation for the Ancillary Documents section.
    - If found, note the paths for inclusion in the PRD.

2. **Research & Validate**

    - **Discover Application Architecture**: Understand the existing codebase to ground requirements in reality:
        - Identify the primary language(s), framework(s), and runtime environment
        - Locate and review project documentation (README, architecture docs, contributing guides)
        - Examine dependency management files to understand the tech stack
        - Survey the project structure to identify organizational patterns (monolith, modular, microservices, etc.)
        - Review coding standards, testing frameworks, and quality tooling already in place
        - Identify similar features or modules already implemented to understand established patterns
    - **Enhanced Package Research**:
        - Use `mcp_perplexity_search` to discover Laravel packages relevant to the feature domain
        - Query for: "Laravel packages for [domain]", "PHP libraries for [functionality]", etc.
        - Use `mcp_Context7_resolve-library-id` and `mcp_Context7_get-library-docs` to evaluate package documentation
        - Use `mcp_deepwiki_ask_question` to get GitHub insights
        - Cross-reference with existing `@packages/` documentation
        - Include recommended packages in the PRD's Technical Architecture section with justification
    - **Knowledge Graph Search**: Use `mcp_newknowledge_aim_search_nodes` to find related concepts, rules, existing features, or prior work to avoid redundancy.
    - **Comprehensive Analysis**:
        - Use `mcp_perplexity_reason` to analyze technical feasibility and architectural fit
        - Use `mcp_perplexity_deep_research` to conduct market analysis and competitive landscape assessment
        - Use `mcp_Context7_get-library-docs` and `mcp_deepwiki_read_wiki_contents` to review technical documentation in-depth
        - **Knowledge Management**: Use `mcp_newknowledge_aim_create_entities` to capture research findings and architectural decisions for future reference
    - **External Validation**: validate assumptions against industry best practices and competing solutions using enhanced research tools.

3. **Draft PRD**

    - Create a new markdown file in `.taskmaster/prds/` with filename `EPIC-XXX_<short-title>.md`.
    - Structure must include:

        - **Title & Epic ID**
        - **Summary**: concise, high-level description of the feature.
        - **Problem Statement**: what user or business problem this solves.
        - **Goals & Non-Goals**: clear success criteria and what is explicitly out of scope.
        - **Planning Documents**:

            - Idea: `.taskmaster/ideas/[filename].md`
            - Discussion: `.taskmaster/discussions/[filename].md` (if exists)

        - **Ancillary Documents**:
          [Any additional reference materials, research files, or external documentation]
        - **Research Findings**: comprehensive analysis from enhanced research tools:
            - Laravel package ecosystem analysis
            - Technical feasibility assessment
            - Market landscape and competitive analysis
            - Architecture compatibility evaluation
        - **User Stories / Scenarios**: examples of how users will interact with the feature.
        - **Requirements** (functional & non-functional).
        - **Technical Architecture**: Document the application's tech stack and architectural constraints that implementation must follow:
            - Primary language(s), framework(s), and versions
            - Database technology and ORM/query layer
            - Architectural pattern (e.g., modular, layered, event-driven)
            - Testing framework and quality standards
            - UI framework or presentation layer (if applicable)
            - Key libraries or packages already in use that this feature must integrate with
            - **Recommended Packages**: List packages from `@packages/` that are relevant to this feature:
                - Package name and URL
                - Why this package is recommended for this feature
                - Key features that address specific requirements
                - Integration considerations or dependencies
            - Coding standards and linting tools
        - **Dependencies & Constraints**: known blockers, integrations, or risks.
        - **Risks & Mitigations**: where this could fail, and how to reduce risk.
        - If anything is unclear or needs clarification, ask the user before proceeding.
        - **Directive to Task Generator**:
            > _Note: The task generation AI must only create tasks explicitly listed in this plan. It must not add any steps for manual peer reviews, pull requests, or merges._

4. **Confirm Draft**
    - Present the PRD content to the user for review and approval.
    - Display planning and ancillary document paths for verification.
    - Only upon approval, save the file to `.taskmaster/prds/`.

---

## Recommend Next Step

After PRD creation, suggest:  
_"The PRD is ready. We can now formalize this into an epic with `create epic for @prds/EPIC-XXX_<short-title>.md`."\_

---

## Forbidden

1. Do not include implementation details, code-level design, or task breakdowns.
2. Do not skip research steps — architecture discovery, enhanced package research, knowledge graph search, and comprehensive analysis are all mandatory.
3. Do not assume or invent the tech stack — it must be discovered from the actual codebase.
4. Do not recommend packages that don't exist in `@packages/` unless absolutely necessary and well-justified.
5. Do not save the PRD without comprehensive research backing and user confirmation.
6. Do not create multiple PRDs at once — only the one specified or derived from the selected idea.
7. **Do not include timelines, milestones or time estimates** — this is agentic programming where time estimates are pointless and quality/completeness are the only metrics that matter
8. Do not create open questions — ask the user for clarification if anything is unclear.
9. Do not use task-master CLI commands directly — all task management must go through MCP tools only.
10. Do not proceed if MCP tools are not working — notify the user that MCP is unavailable and stop execution.
