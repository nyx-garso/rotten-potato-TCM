---
ID: "RP-PRF-0005"
Title: "RP-PRF-0005 — Account Type Handling"
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

# RP-PRF-0005 — Account Type Handling

**Summary:** Verify that account type determines available actions.  

**Preconditions:** Authenticated account.

| # | Step Actions | Expected Results |
|---|--------------|------------------|
| 1 | Log in as Standard Client | Seller-only options are hidden |
| 2 | Log in as Seller account | Seller options (e.g., Post Artwork) are visible |
| 3 | Attempt seller-only action as client | Error/denial message displayed |

## Postconditions

- Tested on https://rotten-potato-tau.vercel.app/homepage using account testuser1@test.com (password: testuser1).
- Cleanup: log out after the test; remove or revert any test data created (posts, requests, payments, profile changes)
- Verify environment returned to pre-test state before running subsequent tests.

