---
ID: RP-PRF-0001
Title: "RP-PRF-0001 \u2014 Profile Display"
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


# RP-PRF-0001 — Profile Display

**Summary:** Verify that profile details (username, email, account type, join date) are displayed correctly.  

**Preconditions:** Authenticated account.

| # | Step Actions | Expected Results |
|---|--------------|------------------|
| 1 | Log in and navigate to Profile page | Profile page loads successfully |
| 2 | Check displayed username and email | Correct values are shown |
| 3 | Check account type and join date | Correct values are shown |

## Postconditions

- Tested on https://rotten-potato-tau.vercel.app/homepage using account testuser1@test.com (password: testuser1).
- Cleanup: log out after the test; remove or revert any test data created (posts, requests, payments, profile changes)
- Verify environment returned to pre-test state before running subsequent tests.

