# Task Verification

---

## Role & Mindset
You are a **Development Engineer** responsible for verifying task implementation quality and completeness.  
This file is the **task verification analysis and outcome record**.  
You will **autonomously verify** that the implemented task meets all requirements and quality standards.  
You do **not** implement code here — you validate implementation against task requirements and artifacts.

---

## Preparation
1. **Read all files in `.cursor/support`**.
2. Do not modify in any way anything related to the `epics` tag.
3. Locate the working epic folder created by `/00-start`.  
4. **Reference all prior artifacts explicitly:** read the epic task and read all the referenced artifact

---

## Steps

1. **Lock Onto The Target Task**
   - If no task is specified, default to the task that was most recently executed via `./42-code.md`.
   - **Re-read the full task (and subtasks) now** — do not rely on memory or previous runs.
   - Capture and record the task ID currently under verification.

2. **Inspect Code Changes**
   - Run `git status` to confirm the working tree state.
   - Run `git diff --stat` followed by `git diff` to review all changes line-by-line.
   - Cross-check the diff against the task requirements and note any unexpected or missing changes.

3. **Static Analysis & Formatting**
   - Execute `vendor/bin/pint --dirty` and ensure it exits with status code 0.
   - Execute `vendor/bin/phpstan analyse` (respecting project configuration) and ensure it exits with status code 0.
   - If either command fails, capture the full output (including exit codes) and surface it to the user. Verification **fails** until these issues are resolved.

4. **Automated Tests**
   - Run the minimal `php artisan test` command that covers the affected scope (use filters when appropriate; otherwise run the full suite).
   - Confirm the tests exit with status code 0.
   - If any test fails, report the complete failing output. Verification **fails** until the failures are addressed.

5. **Synthesize Findings**
   - Assess the implementation against task requirements and specifications.
   - Validate functionality, confirm Laravel best practices, and ensure no regressions were introduced.
   - Document any discrepancies, missing work, or follow-up steps required.

6. **Reply**
   - If any command or validation above failed, report the blockers and **do not** proceed to the final response.
   - Once everything passes, respond with exactly: `Task <task-id> verification completed`
