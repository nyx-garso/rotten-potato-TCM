---
ID: RP-MSG-0001
Title: Test Case: RP-MSG-0001 | Target User Profile Lookup Execution
Priority: Medium
Status: draft
Automated: no
Owner: 
Requirements: 
Postconditions: "- Tested on https://rotten-potato-tau.vercel.app/homepage using account testuser1@test.com (password: testuser1).
- Cleanup: log out after the test; remove or revert any test data created (posts, requests, payments, profile changes)
- Verify environment returned to pre-test state before running subsequent tests."
---
# Test Case: RP-MSG-0001 | Target User Profile Lookup Execution

**Summary:** Verify that inputting user parameters inside search fields surfaces relevant profile directories.

**Preconditions:** Directory lookup text input element is loaded.

| # | Step Actions | Expected Results |
|---|---|---|
| 1 | Provide a valid search text query criteria inside the messaging user search element, then hit the Enter key. | System updates the workspace sub-panel layout view to render profile matches. |

## Postconditions

- Tested on https://rotten-potato-tau.vercel.app/homepage using account testuser1@test.com (password: testuser1).
- Cleanup: log out after the test; remove or revert any test data created (posts, requests, payments, profile changes)
- Verify environment returned to pre-test state before running subsequent tests.

