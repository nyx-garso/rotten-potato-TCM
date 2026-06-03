---
ID: RP-PRF-0004
Title: RP-PRF-0004 — Edit Profile (Cancel)
Priority: Medium
Status: draft
Automated: no
Owner: 
Requirements: 
Postconditions: "- Tested on https://rotten-potato-tau.vercel.app/homepage using account testuser1@test.com (password: testuser1).
- Cleanup: log out after the test; remove or revert any test data created (posts, requests, payments, profile changes)
- Verify environment returned to pre-test state before running subsequent tests."
---
# RP-PRF-0004 — Edit Profile (Cancel)

**Summary:** Verify that canceling edits does not change profile data.  

**Preconditions:** Authenticated account.

| # | Step Actions | Expected Results |
|---|--------------|------------------|
| 1 | Navigate to Edit Profile | Edit form loads |
| 2 | Change username/email but click Cancel | No changes saved |
| 3 | Reload profile page | Original values remain unchanged |

## Postconditions

- Tested on https://rotten-potato-tau.vercel.app/homepage using account testuser1@test.com (password: testuser1).
- Cleanup: log out after the test; remove or revert any test data created (posts, requests, payments, profile changes)
- Verify environment returned to pre-test state before running subsequent tests.

