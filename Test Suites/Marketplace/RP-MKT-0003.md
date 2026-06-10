---
ID: RP-MKT-0003
Title: 'Test Case: RP-MKT-0003 | Ask Artist Control Availability and Browse Stability'
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


# Test Case: RP-MKT-0003 | Ask Artist Control Availability and Browse Stability

**Summary:** Verify that marketplace artwork cards expose an Ask Artist action and keep the browse layout stable.

**Preconditions:** Marketplace catalog is loaded and an artwork card is visible.

| # | Step Actions | Expected Results |
|---|---|---|
| 1 | Inspect the visible artwork card actions. | System displays the Ask Artist control alongside the Buy action. |
| 2 | Use the Ask Artist control. | System keeps the user on the Marketplace browse surface without breaking the catalog layout. |

## Postconditions

- Tested on https://rotten-potato-tau.vercel.app/homepage using account testuser1@test.com (password: testuser1).
- Cleanup: log out after the test; remove or revert any test data created (posts, requests, payments, profile changes)
- Verify environment returned to pre-test state before running subsequent tests.

