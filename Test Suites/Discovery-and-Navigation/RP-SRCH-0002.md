---
ID: RP-SRCH-0002
Title: Test Case: RP-SRCH-0002 | Search Tag Filtering Processing
Priority: Medium
Status: draft
Automated: no
Owner: 
Requirements: 
Postconditions: "- Tested on https://rotten-potato-tau.vercel.app/homepage using account testuser1@test.com (password: testuser1).
- Cleanup: log out after the test; remove or revert any test data created (posts, requests, payments, profile changes)
- Verify environment returned to pre-test state before running subsequent tests."
---
# Test Case: RP-SRCH-0002 | Search Tag Filtering Processing

**Summary:** Verify that updating explicit filter criterion filters listings dynamically in the user panel.

**Preconditions:** User workspace is currently viewing active search results.

| # | Step Actions | Expected Results |
|---|---|---|
| 1 | Toggle and select available category metadata criteria filter choices (e.g., specific art style, art type, pricing boundaries). | System processes the filter parameters and restricts the active records matching the selections. |

## Postconditions

- Tested on https://rotten-potato-tau.vercel.app/homepage using account testuser1@test.com (password: testuser1).
- Cleanup: log out after the test; remove or revert any test data created (posts, requests, payments, profile changes)
- Verify environment returned to pre-test state before running subsequent tests.

