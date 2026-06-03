---
ID: "RP-PAY-0005"
Title: "Test Case: RP-PAY-0005 | Payment Gateways Sub-panel Transitions"
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

# Test Case: RP-PAY-0005 | Payment Gateways Sub-panel Transitions

**Summary:** Verify that advancing from delivery data triggers payment method integrations.

**Preconditions:** Shipping data entry fields are populated and verified.

| # | Step Actions | Expected Results |
|---|---|---|
| 1 | Click the designated "Proceed to Payment" action control item. | System transitions the active view layout step to expose all integrated payment channels. |

## Postconditions

- Tested on https://rotten-potato-tau.vercel.app/homepage using account testuser1@test.com (password: testuser1).
- Cleanup: log out after the test; remove or revert any test data created (posts, requests, payments, profile changes)
- Verify environment returned to pre-test state before running subsequent tests.

