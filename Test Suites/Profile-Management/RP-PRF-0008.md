---
ID: "RP-PRF-0008"
Title: "RP-PRF-0008 — Become a Seller (Upgrade Flow)"
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

# RP-PRF-0008 — Become a Seller (Upgrade Flow)

**Summary:** Verify that a client can upgrade their account to a seller. 
 
**Preconditions:** Authenticated account with Standard Client type.

| # | Step Actions | Expected Results |
|---|--------------|------------------|
| 1 | Log in as Standard Client | Profile page loads with “Become a Seller” option |
| 2 | Click “Become a Seller” | Seller upgrade form loads |
| 3 | Fill required seller details and submit | Success message displayed |
| 4 | Reload profile page | Account type updated to Seller, seller options visible |

## Postconditions

- Tested on https://rotten-potato-tau.vercel.app/homepage using account testuser1@test.com (password: testuser1).
- Cleanup: log out after the test; remove or revert any test data created (posts, requests, payments, profile changes)
- Verify environment returned to pre-test state before running subsequent tests.

