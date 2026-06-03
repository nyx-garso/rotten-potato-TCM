---
ID: "RP-REV-0002"
Title: "Test Case: RP-REV-0002 | Zero-Review Count Display"
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

# Test Case: RP-REV-0002 | Zero-Review Count Display

**Summary:** Verify that an artwork with no reviews still renders its rating metadata clearly.

**Preconditions:** Marketplace catalog is loaded.

| # | Step Actions | Expected Results |
|---|---|---|
| 1 | View an artwork card that has no recorded reviews. | System displays the rating summary and a zero review count instead of hiding the reputation area. |

## Postconditions

- Tested on https://rotten-potato-tau.vercel.app/homepage using account testuser1@test.com (password: testuser1).
- Cleanup: log out after the test; remove or revert any test data created (posts, requests, payments, profile changes)
- Verify environment returned to pre-test state before running subsequent tests.

