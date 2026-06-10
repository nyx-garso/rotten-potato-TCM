---
ID: RP-PRF-0009
Title: "RP-PRF-0009 \u2014 Become a Seller (Validation & Restrictions)"
Priority: Medium
Status: draft
Automated: 'no'
Owner: ''
Requirements: ''
Postconditions: '- Tested on https://rotten-potato-tau.vercel.app/homepage using account
  testuser1@test.com (password: testuser1).

  - Cleanup: log out after the test; remove or revert any test data created (posts,
  requests, payments, profile changes)

  - Verify environment returned to pre-test state before running subsequent tests.

  '
Test Schedule: 2026/03/23
---


# RP-PRF-0009 — Become a Seller (Validation & Restrictions)

**Summary:** Verify validation and restrictions during seller upgrade.  

**Preconditions:** Authenticated account with Standard Client type.

| # | Step Actions | Expected Results |
|---|--------------|------------------|
| 1 | Click “Become a Seller” without filling required fields | Error messages displayed, form not submitted |
| 2 | Attempt to upgrade with invalid data (e.g., invalid ID number) | Validation error displayed |
| 3 | Attempt to upgrade when already a Seller | “Already a Seller” message displayed, no duplicate upgrade |

## Postconditions

- Tested on https://rotten-potato-tau.vercel.app/homepage using account testuser1@test.com (password: testuser1).
- Cleanup: log out after the test; remove or revert any test data created (posts, requests, payments, profile changes)
- Verify environment returned to pre-test state before running subsequent tests.

