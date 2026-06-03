---
ID: RP-COMM-0005
Title: Test Case: RP-COMM-0005 | Commission Board Default View and Tab Switching
Priority: Medium
Status: draft
Automated: no
Owner: 
Requirements: 
Postconditions: "- Tested on https://rotten-potato-tau.vercel.app/homepage using account testuser1@test.com (password: testuser1).
- Cleanup: log out after the test; remove or revert any test data created (posts, requests, payments, profile changes)
- Verify environment returned to pre-test state before running subsequent tests."
---
# Test Case: RP-COMM-0005 | Commission Board Default View and Tab Switching

**Summary:** Verify that the Commission board loads with browse and personal request tabs available.

**Preconditions:** Authenticated user session is available.

| # | Step Actions | Expected Results |
|---|---|---|
| 1 | Click the Commission button from the main navigation. | System opens the Commission board with the page heading, browse tab, and personal requests tab visible. |
| 2 | Click the Browse Requests tab and then click the My Requests tab. | System switches the active board section for each tab selection without losing the page context. |

## Postconditions

- Tested on https://rotten-potato-tau.vercel.app/homepage using account testuser1@test.com (password: testuser1).
- Cleanup: log out after the test; remove or revert any test data created (posts, requests, payments, profile changes)
- Verify environment returned to pre-test state before running subsequent tests.

