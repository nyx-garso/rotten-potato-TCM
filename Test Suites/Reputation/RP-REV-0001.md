---
ID: "RP-REV-0001"
Title: "Test Case: RP-REV-0001 | Artwork Rating Visibility"
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

# Test Case: RP-REV-0001 | Artwork Rating Visibility

**Summary:** Verify that marketplace artwork cards display rating metadata in the live release.

**Preconditions:** Marketplace catalog is loaded and at least one artwork card is visible.

| # | Step Actions | Expected Results |
|---|---|---|
| 1 | Inspect a visible artwork card in the Marketplace. | System shows the star rating value and review count for the artwork. |

## Postconditions

- Tested on https://rotten-potato-tau.vercel.app/homepage using account testuser1@test.com (password: testuser1).
- Cleanup: log out after the test; remove or revert any test data created (posts, requests, payments, profile changes)
- Verify environment returned to pre-test state before running subsequent tests.

