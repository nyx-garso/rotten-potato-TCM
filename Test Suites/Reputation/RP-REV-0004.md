---
ID: "RP-REV-0004"
Title: "Test Case: RP-REV-0004 | Rating Metadata Persists Across Filters"
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

# Test Case: RP-REV-0004 | Rating Metadata Persists Across Filters

**Summary:** Verify that category and sort changes do not remove the displayed rating values from the returned artwork cards.

**Preconditions:** Marketplace catalog is loaded.

| # | Step Actions | Expected Results |
|---|---|---|
| 1 | Change the Marketplace category and sort selectors. | System refreshes the catalog while keeping the rating metadata visible on returned results. |

## Postconditions

- Tested on https://rotten-potato-tau.vercel.app/homepage using account testuser1@test.com (password: testuser1).
- Cleanup: log out after the test; remove or revert any test data created (posts, requests, payments, profile changes)
- Verify environment returned to pre-test state before running subsequent tests.

