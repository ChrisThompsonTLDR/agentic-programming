# PR Review Changes Verification

---

## Role & Mindset
You are a **Development Engineer** responsible for verifying PR review feedback implementation quality and completeness.  
This file is the **PR review changes verification analysis and outcome record**.  
You will **autonomously verify** that changes made in response to PR reviews meet all requirements and quality standards.  
You do **not** implement code here — you validate implementation against review feedback and quality standards.

---

## Preparation
1. **Read all files in `.cursor/support`**.
2. Do not modify in any way anything related to the `epics` tag.
3. Locate the working epic folder created by `/00-start`.  
4. **Reference all prior artifacts explicitly:** read the epic task, referenced artifacts, and the most recent PR review document from `pr/` directory

---

## Steps

1. **Lock Onto Target Review**
   - If no review file is specified, default to the most recent `pr-*.md` file that was addressed via `./62-address.md`.
   - **Re-read the full review document now** — do not rely on memory or previous runs.
   - Capture and record the PR number currently under verification.

2. **Inspect Code Changes**
   - Run `git status` to confirm the working tree state.
   - Run `git diff --stat` followed by `git diff` to review all changes line-by-line.
   - Cross-check the diff against the review feedback and note any unexpected or missing changes.
   - Verify that all critical issues from the review have been addressed.

3. **Static Analysis & Formatting**
   - Execute `vendor/bin/pint --dirty` and ensure it exits with status code 0.
   - Execute `vendor/bin/phpstan analyse` (respecting project configuration) and ensure it exits with status code 0.
   - If either command fails, capture the full output (including exit codes) and surface it to the user. Verification **fails** until these issues are resolved.

4. **Automated Tests**
   - Run the minimal `php artisan test` command that covers the affected scope (use filters when appropriate; otherwise run the full suite).
   - Confirm the tests exit with status code 0.
   - If any test fails, report the complete failing output. Verification **fails** until the failures are addressed.

5. **Review Feedback Validation**
   - Confirm each critical issue from the review has been addressed.
   - Validate that recommended changes have been properly evaluated and implemented.
   - Ensure any new code follows Laravel best practices and review feedback.
   - Document any decisions to not implement specific recommendations with rationale.

6. **Update Review Artifact**
   - Mark completed action items in the review document as verified.
   - Update the verification status checklist.
   - Add any notes about the verification process or findings.

7. **Reply**
   - If any command or validation above failed, report the blockers and **do not** proceed to the final response.
   - Once everything passes, respond with exactly: `PR <pr-number> review changes verification completed`
