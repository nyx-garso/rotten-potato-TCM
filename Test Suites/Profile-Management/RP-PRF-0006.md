---
ID: "RP-PRF-0006"
Title: "RP-PRF-0006 — Recent Activity Logging"
Priority: "Medium"
Status: "draft"
Automated: "no"
Owner: ""
Requirements: ""
Postconditions: |
  - Tested on https://rotten-potato-tau.vercel.app/homepage using account testuser1@test.com (password: testuser1).
  - Cleanup: log out after the test; remove or revert any test data created (posts, requests, payments, profile changes)
  - Verify environment returned to pre-test state before running subsequent tests.
---

# RP-PRF-0006 — Recent Activity Logging

**Summary:** Verify that actions are logged in Recent Activity.  

**Preconditions:** Authenticated account.

| # | Step Actions | Expected Results |
|---|--------------|------------------|
| 1 | Perform commission request | Entry appears in Recent Activity |
| 2 | Purchase artwork | Entry appears in Recent Activity |
| 3 | Save item to favorites | Entry appears in Recent Activity |

## Postconditions

- Tested on https://rotten-potato-tau.vercel.app/homepage using account testuser1@test.com (password: testuser1).
- Cleanup: log out after the test; remove or revert any test data created (posts, requests, payments, profile changes)
- Verify environment returned to pre-test state before running subsequent tests.

