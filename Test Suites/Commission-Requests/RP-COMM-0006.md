---
ID: RP-COMM-0006
Title: Test Case: RP-COMM-0006 | Commission Request List Segmentation
Priority: Medium
Status: draft
Automated: no
Owner: 
Requirements: 
Postconditions: "- Tested on https://rotten-potato-tau.vercel.app/homepage using account testuser1@test.com (password: testuser1).
- Cleanup: log out after the test; remove or revert any test data created (posts, requests, payments, profile changes)
- Verify environment returned to pre-test state before running subsequent tests."
---
# Test Case: RP-COMM-0006 | Commission Request List Segmentation

**Summary:** Verify that the commission board separates open requests from the user-owned request view.

**Preconditions:** Commission board page is open.

| # | Step Actions | Expected Results |
|---|---|---|
| 1 | Open the Browse Requests section on the commission board. | System displays the open commission listing area and loads the available request feed state. |
| 2 | Open the My Requests section on the commission board. | System displays the user-specific request list area instead of the open request feed. |

## Postconditions

- Tested on https://rotten-potato-tau.vercel.app/homepage using account testuser1@test.com (password: testuser1).
- Cleanup: log out after the test; remove or revert any test data created (posts, requests, payments, profile changes)
- Verify environment returned to pre-test state before running subsequent tests.

