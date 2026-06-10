---
ID: RP-PAY-0006
Title: 'Test Case: RP-PAY-0006 | Checkout Disabled With No Selection'
Priority: Medium
Status: draft
Automated: 'no'
Owner: ''
Requirements: ''
Postconditions: '- Tested on https://rotten-potato-tau.vercel.app/homepage using account
  testuser1@test.com (password: testuser1).

  - Cleanup: re-select cart items if continuing with checkout tests.

  - Log out after testing when no further authenticated tests are queued.

  '
Test Schedule: 2026/03/23
---


﻿---
ID: "RP-PAY-0006"
Title: "Test Case: RP-PAY-0006 | Checkout Disabled With No Selection"
Priority: "Medium"
Status: "ready"
Automated: "no"
Owner: ""
Requirements: ""
Postconditions: |
  - Tested on https://rotten-potato-tau.vercel.app/homepage using account testuser1@test.com (password: testuser1).
  - Cleanup: re-select cart items if continuing with checkout tests.
  - Log out after testing when no further authenticated tests are queued.
---

# Test Case: RP-PAY-0006 | Checkout Disabled With No Selection

**Summary:** Verify that checkout cannot be started when no cart item is selected.

**Preconditions:** User is logged in and the `/cart` page displays at least one cart item.

| # | Step Actions | Expected Results |
|---|---|---|
| 1 | Clear all selected cart item checkboxes, or click `Select All` when all items are selected. | No cart items remain selected. |
| 2 | Observe the `Order Summary` panel. | The subtotal shows `0 items`, the total reflects no selected merchandise, and `Proceed to Checkout (0)` is disabled. |
| 3 | Attempt to start checkout without selecting an item. | The disabled checkout button prevents submission; no PayMongo checkout session is created. |

## Postconditions

- Tested on https://rotten-potato-tau.vercel.app/homepage using account testuser1@test.com (password: testuser1).
- Cleanup: re-select cart items if continuing with checkout tests.
- Log out after testing when no further authenticated tests are queued.
