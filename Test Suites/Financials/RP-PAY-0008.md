---
ID: "RP-PAY-0008"
Title: "Test Case: RP-PAY-0008 | Final Transaction Commit and Order Dispatch"
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

# Test Case: RP-PAY-0008 | Final Transaction Commit and Order Dispatch

**Summary:** Verify that confirming the transaction changes order lifecycle indicators and forwards data targets to the seller context.

**Preconditions:** Order details are locked in the static review view container.

| # | Step Actions | Expected Results |
|---|---|---|
| 1 | Click the "Place Order" workflow submission button. | System finalizes order processing states, stores records, and dispatches invoice data records directly to the specific artist account context. |

## Postconditions

- Tested on https://rotten-potato-tau.vercel.app/homepage using account testuser1@test.com (password: testuser1).
- Cleanup: log out after the test; remove or revert any test data created (posts, requests, payments, profile changes)
- Verify environment returned to pre-test state before running subsequent tests.

