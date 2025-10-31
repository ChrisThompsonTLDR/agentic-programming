# PR Review Changes Commit

---

## Role & Mindset
You are a **Development Engineer** responsible for committing and pushing PR review feedback changes.  
This file is the **PR review changes commit and push record**.  
You will **autonomously commit and push** changes made in response to PR reviews after verification.  
You do **not** implement new code here — you finalize and commit verified changes.

---

## Preparation
1. **Read all files in `.cursor/support`**.
2. Do not modify in any way anything related to the `epics` tag
3. Locate the working epic folder created by `/00-start`.  
4. **Reference all prior artifacts explicitly:** read the epic task, referenced artifacts, and the most recent PR review document from `pr/` directory

---

## Steps

1. **Verify Changes Readiness**
   - If no review file is specified, use the most recent `pr-*.md` file that was verified through ./63-verify.md
   - Confirm all changes have passed comprehensive verification.
   - Ensure all review feedback has been properly addressed.
   - Verify final compliance with Laravel standards and review requirements.

2. **Git Commit**
   - Stage all changes with `git add .`
   - Create a commit with the implemented changes.
   - Use a descriptive title that summarizes the review feedback addressed.
   - Include in the commit body:
     - PR number
     - Epic ID or reference
     - Task ID (if applicable)
     - Summary of review feedback addressed
   - Commit format example:
     ```
     Addressed PR review feedback
     
     PR: #<pr-number>
     Epic: [epic-id]
     Task: [task-id] (if applicable)
     
     - Fixed [issue 1]
     - Improved [issue 2]
     - Updated [issue 3]
     ```

3. **Git Push**
   - Push the commit to the remote repository.
   - Use `git push` to update the PR branch.
   - Verify the push was successful.
   - Confirm the remote branch is updated.

4. **Update Review Artifact**
   - Update the review document to indicate changes have been committed and pushed.
   - Add the commit SHA to the review artifact for traceability.
   - Mark the review cycle as complete.

5. **Reply**
   - `PR <pr-number> review changes committed and pushed`  
   - Exactly that and nothing else
