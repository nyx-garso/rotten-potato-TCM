---
ID: "RP-PRF-0003"
Title: "RP-PRF-0003 — Edit Profile (Persistence)"
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

# RP-PRF-0003 — Edit Profile (Persistence)

**Summary:** Verify that profile edits persist after saving.  

**Preconditions:** Authenticated account.

| # | Step Actions | Expected Results |
|---|--------------|------------------|
| 1 | Navigate to Edit Profile | Edit form loads |
| 2 | Change username/email and click Save | Success message displayed |
| 3 | Reload profile page | Updated values persist |

## Postconditions

- Tested on https://rotten-potato-tau.vercel.app/homepage using account testuser1@test.com (password: testuser1).
- Cleanup: log out after the test; remove or revert any test data created (posts, requests, payments, profile changes)
- Verify environment returned to pre-test state before running subsequent tests.

