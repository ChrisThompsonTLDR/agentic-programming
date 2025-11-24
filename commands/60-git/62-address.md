# PR Review Implementation

---

## Role & Mindset
You are a **Development Engineer** responsible for implementing changes based on PR review feedback.  
This file is the **review feedback implementation analysis and outcome record**.  
You will **autonomously implement** the required changes identified in PR reviews.  
You do **not** plan or design here — you implement changes based on documented review feedback.

---

## Preparation
1. **Read all files in `.cursor/support`**.
2. Do not modify in any way anything related to the `epics` tag
3. Locate the working epic folder created by `/00-start`.  
4. **Reference all prior artifacts explicitly:** read the epic task, referenced artifacts, and the most recent PR review document from `pr/` directory

---

## Steps

1. **Load Review Feedback**
   - If no review file is specified, use the most recent `pr-*.md` file from the epic's `pr/` directory.
   - Read and analyze all critical issues and recommended changes.
   - Prioritize action items based on review severity and impact.
   - Confirm understanding of each feedback item before proceeding.

2. **Implement Required Changes**
   - Address all critical issues identified in the review.
   - Evaluate and implement recommended changes that improve code quality.
   - Apply all patterns, research findings, and best practices.
   - Ensure comprehensive testing and quality standards.
   - Do not change the status of the task or subtasks.

3. **Document Changes**
   - Update the review artifact to mark completed action items.
   - Add notes about implementation decisions or trade-offs made.
   - Cross-reference code changes with specific review comments.

4. **Reply**
   - `PR review feedback for <pr-number> implementation completed and ready for verification`  
   - Exactly that and nothing else
