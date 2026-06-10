---
ID: RP-MKT-0001
Title: 'Test Case: RP-MKT-0001 | Marketplace Landing and Search Controls'
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


# Test Case: RP-MKT-0001 | Marketplace Landing and Search Controls

**Summary:** Verify that the Marketplace page loads with the catalog search, category, and sort controls visible.

**Preconditions:** Authenticated user session is available.

| # | Step Actions | Expected Results |
|---|---|---|
| 1 | Click the Marketplace button from the main navigation. | System opens the Marketplace catalog view with the browse header, search field, category selector, and sort selector visible. |
| 2 | Click inside the search box and enter a valid artwork or artist query. | System accepts the query and begins updating the catalog results area for the matching records. |

## Postconditions

- Tested on https://rotten-potato-tau.vercel.app/homepage using account testuser1@test.com (password: testuser1).
- Cleanup: log out after the test; remove or revert any test data created (posts, requests, payments, profile changes)
- Verify environment returned to pre-test state before running subsequent tests.

