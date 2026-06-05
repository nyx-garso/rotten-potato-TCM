---
ID: "RP-MSG-0004"
Title: "Test Case: RP-MSG-0004 | Local Binary Object Media Upload Gateways"
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

# Test Case: RP-MSG-0004 | Local Binary Object Media Upload Gateways

**Summary:** Verify that clicking file attachment indicators displays system document selection tools.

**Preconditions:** Communication interface session is initialized.

| # | Step Actions | Expected Results |
|---|---|---|
| 1 | Click the file attachment paperclip component link node inside the chat input layout. | System opens local storage access dialog interfaces, allowing selections of photos or videos for upload. |

## Postconditions

- Tested on https://rotten-potato-tau.vercel.app/homepage using account testuser1@test.com (password: testuser1).
- Cleanup: log out after the test; remove or revert any test data created (posts, requests, payments, profile changes)
- Verify environment returned to pre-test state before running subsequent tests.

