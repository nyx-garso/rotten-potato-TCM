---
ID: "RP-PAY-0008"
Title: "Test Case: RP-PAY-0008 | PayMongo Paid Webhook Order Commit"
Priority: "High"
Status: "ready"
Automated: "no"
Owner: ""
Requirements: ""
Postconditions: |
  - Tested on https://rotten-potato-tau.vercel.app/homepage using account testuser1@test.com (password: testuser1).
  - Cleanup: remove/revert any test payments, notifications, stock changes, and cart changes created by the webhook test.
  - Log out after testing when no further authenticated tests are queued.
---

# Test Case: RP-PAY-0008 | PayMongo Paid Webhook Order Commit

**Summary:** Verify that a successful PayMongo checkout webhook commits payment state, updates artwork inventory, notifies the artist, and clears the buyer cart.

**Preconditions:** A PayMongo checkout session was created from selected cart items and its metadata contains a valid `payment_id` and `buyer_id`.

| # | Step Actions | Expected Results |
|---|---|---|
| 1 | Complete the PayMongo checkout | The webhook endpoint accepts the paid event and returns `{ "received": true }` with HTTP 200. |
| 2 | Verify the matching payment record. | The `payments` row matching `payment_id` is updated to `status = paid` and receives a current `transaction_date`. |
| 3 | Verify each purchased artwork referenced by the paid session line items. | The artwork stock quantity is decremented by the purchased quantity; if stock reaches `0`, artwork status becomes `sold`, otherwise it remains available. |
| 4 | Verify seller notification behavior. | The artwork owner receives a `purchase` notification containing the buyer actor id, artwork entity id, artwork entity type, purchased title, and quantity. |
| 5 | Verify buyer cart cleanup. | If selected cart item metadata exists, only those checked `cart_items` rows are removed for the webhook `buyer_id`; if metadata is absent, the implementation falls back to clearing all cart rows for that buyer. |

## Postconditions

- Tested on https://rotten-potato-tau.vercel.app/homepage using account testuser1@test.com (password: testuser1).
- Cleanup: remove/revert any test payments, notifications, stock changes, and cart changes created by the webhook test.
- Log out after testing when no further authenticated tests are queued.
