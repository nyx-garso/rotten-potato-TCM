---
ID: RP-PAY-0003
Title: 'Test Case: RP-PAY-0003 | Selective Checkout Item Selection'
Priority: Medium
Status: draft
Automated: 'no'
Owner: ''
Requirements: ''
Postconditions: '- Tested on https://rotten-potato-tau.vercel.app/homepage using account
  testuser1@test.com (password: testuser1).

  - Cleanup: restore the original selected-item state if continuing with checkout
  tests.

  - Log out after testing when no further authenticated tests are queued.

  '
Test Schedule: 2026/03/23
---


﻿---
ID: "RP-PAY-0003"
Title: "Test Case: RP-PAY-0003 | Selective Checkout Item Selection"
Priority: "Medium"
Status: "ready"
Automated: "no"
Owner: ""
Requirements: ""
Postconditions: |
  - Tested on https://rotten-potato-tau.vercel.app/homepage using account testuser1@test.com (password: testuser1).
  - Cleanup: restore the original selected-item state if continuing with checkout tests.
  - Log out after testing when no further authenticated tests are queued.
---

# Test Case: RP-PAY-0003 | Selective Checkout Item Selection

**Summary:** Verify that item checkboxes control which cart items are included in checkout totals.

**Preconditions:** User is logged in and the `/cart` page displays at least one cart item.

| # | Step Actions | Expected Results |
|---|---|---|
| 1 | Observe the cart immediately after loading. | All current cart items are selected by default, and the `Proceed to Checkout (#)` button count matches the number of selected items. |
| 2 | Clear one item checkbox or use `Select All` to toggle selection. | The selected-item count in `Subtotal (# items)` and `Proceed to Checkout (#)` updates to match the checked items. |
| 3 | Re-select the item or use `Select All` again. | The item is included again in the subtotal and checkout button count. |

## Postconditions

- Tested on https://rotten-potato-tau.vercel.app/homepage using account testuser1@test.com (password: testuser1).
- Cleanup: restore the original selected-item state if continuing with checkout tests.
- Log out after testing when no further authenticated tests are queued.
