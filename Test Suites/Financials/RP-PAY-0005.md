---
ID: RP-PAY-0005
Title: 'Test Case: RP-PAY-0005 | Cart Item Removal and Empty State'
Priority: Medium
Status: draft
Automated: 'no'
Owner: ''
Requirements: ''
Postconditions: '- Tested on https://rotten-potato-tau.vercel.app/homepage using account
  testuser1@test.com (password: testuser1).

  - Cleanup: re-add removed test items if needed for later checkout tests.

  - Log out after testing when no further authenticated tests are queued.

  '
Test Schedule: 2026/03/23
---


﻿---
ID: "RP-PAY-0005"
Title: "Test Case: RP-PAY-0005 | Cart Item Removal and Empty State"
Priority: "Medium"
Status: "ready"
Automated: "no"
Owner: ""
Requirements: ""
Postconditions: |
  - Tested on https://rotten-potato-tau.vercel.app/homepage using account testuser1@test.com (password: testuser1).
  - Cleanup: re-add removed test items if needed for later checkout tests.
  - Log out after testing when no further authenticated tests are queued.
---

# Test Case: RP-PAY-0005 | Cart Item Removal and Empty State

**Summary:** Verify that users can remove cart items and receive the correct empty-cart message when no items remain.

**Preconditions:** User is logged in and the `/cart` page displays at least one cart item that may be safely removed.

| # | Step Actions | Expected Results |
|---|---|---|
| 1 | Click the remove/trash button on a cart item. | The item row is temporarily disabled while updating, then the item is removed from the cart list and selected-item totals are recalculated. |
| 2 | If multiple items remain, remove each remaining test item. | The cart list continues to update without requiring a full page reload. |
| 3 | Observe the page when the cart has no items. | The empty state appears with `Your cart is empty`, explanatory text, and a `Continue Shopping` button that routes back to `/homepage`. |

## Postconditions

- Tested on https://rotten-potato-tau.vercel.app/homepage using account testuser1@test.com (password: testuser1).
- Cleanup: re-add removed test items if needed for later checkout tests.
- Log out after testing when no further authenticated tests are queued.
