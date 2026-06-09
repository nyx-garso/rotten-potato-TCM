---
ID: "RP-REV-0005"
Title: "Test Case: RP-REV-0005 | Rating Metadata and Price Cohesion"
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

# Test Case: RP-REV-0005 | Rating Metadata and Price Cohesion

**Summary:** Verify that artwork rating details remain grouped with the title, artist, and price on the marketplace card.

**Preconditions:** Marketplace catalog is loaded and a result card is visible.

| # | Step Actions | Expected Results |
|---|---|---|
| 1 | Inspect a loaded marketplace artwork card after the page finishes rendering. | System presents the artwork title, artist, rating, review count, and price together on the same card. |

## Postconditions

- Tested on https://rotten-potato-tau.vercel.app/homepage using account testuser1@test.com (password: testuser1).
- Cleanup: log out after the test; remove or revert any test data created (posts, requests, payments, profile changes)
- Verify environment returned to pre-test state before running subsequent tests.

