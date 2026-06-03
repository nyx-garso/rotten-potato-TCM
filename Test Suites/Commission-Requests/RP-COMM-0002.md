---
ID: "RP-COMM-0002"
Title: "Test Case: RP-COMM-0002 | Public Commission Feed Ingestion"
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

# Test Case: RP-COMM-0002 | Public Commission Feed Ingestion

**Summary:** Verify that submitting job properties appends requirements onto open commission feeds.

**Preconditions:** Requirement definitions form input structures contain text specifications.

| # | Step Actions | Expected Results |
|---|---|---|
| 1 | Click the final "Post Commission" form submission workflow controller button. | System saves the database requirements listing and updates the public board to render it at the top of the chronological feed. |

## Postconditions

- Tested on https://rotten-potato-tau.vercel.app/homepage using account testuser1@test.com (password: testuser1).
- Cleanup: log out after the test; remove or revert any test data created (posts, requests, payments, profile changes)
- Verify environment returned to pre-test state before running subsequent tests.

