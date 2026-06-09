---
ID: "RP-REV-0003"
Title: "Test Case: RP-REV-0003 | Rating Metadata Follows Search Results"
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

# Test Case: RP-REV-0003 | Rating Metadata Follows Search Results

**Summary:** Verify that rating metadata stays attached to the matching artwork card after a search.

**Preconditions:** Marketplace catalog search field is responsive.

| # | Step Actions | Expected Results |
|---|---|---|
| 1 | Search for a valid artwork name or artist name. | System returns the matching artwork card with its rating metadata still visible. |

## Postconditions

- Tested on https://rotten-potato-tau.vercel.app/homepage using account testuser1@test.com (password: testuser1).
- Cleanup: log out after the test; remove or revert any test data created (posts, requests, payments, profile changes)
- Verify environment returned to pre-test state before running subsequent tests.

