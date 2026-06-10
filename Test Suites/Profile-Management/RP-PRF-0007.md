---
ID: RP-PRF-0007
Title: "RP-PRF-0007 \u2014 Recent Activity (Empty State)"
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



# RP-PRF-0007 — Recent Activity (Empty State)

**Summary:** Verify that empty activity shows fallback message.  

**Preconditions:** Authenticated account with no activity.

| # | Step Actions | Expected Results |
|---|--------------|------------------|
| 1 | Log in with new account | Profile page loads |
| 2 | Navigate to Recent Activity section | “No recent activity” message displayed |

## Postconditions

- Tested on https://rotten-potato-tau.vercel.app/homepage using account testuser1@test.com (password: testuser1).
- Cleanup: log out after the test; remove or revert any test data created (posts, requests, payments, profile changes)
- Verify environment returned to pre-test state before running subsequent tests.

