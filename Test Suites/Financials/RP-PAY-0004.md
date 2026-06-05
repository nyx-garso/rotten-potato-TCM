---
ID: "RP-PAY-0004"
Title: "Test Case: RP-PAY-0004 | Cart Quantity Controls"
Priority: "Medium"
Status: "ready"
Automated: "no"
Owner: ""
Requirements: ""
Postconditions: |
  - Tested on https://rotten-potato-tau.vercel.app/homepage using account testuser1@test.com (password: testuser1).
  - Cleanup: return edited quantities to their original values.
  - Log out after testing when no further authenticated tests are queued.
---

# Test Case: RP-PAY-0004 | Cart Quantity Controls

**Summary:** Verify that cart quantity controls update item quantity and order totals.

**Preconditions:** User is logged in and the `/cart` page displays at least one selected cart item.

| # | Step Actions | Expected Results |
|---|---|---|
| 1 | Click the `+` quantity control for a cart item. | The item row is temporarily disabled while updating, then the displayed quantity increases by one. |
| 2 | Review the `Order Summary`. | The subtotal and total update based on the selected item price multiplied by the new quantity. Shipping remains `Free`. |
| 3 | Click the `-` quantity control until the item reaches quantity `1`. | Quantity does not drop below `1`; the decrement control is disabled at the minimum quantity. |

## Postconditions

- Tested on https://rotten-potato-tau.vercel.app/homepage using account testuser1@test.com (password: testuser1).
- Cleanup: return edited quantities to their original values.
- Log out after testing when no further authenticated tests are queued.
