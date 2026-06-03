---
ID: "RP-PAY-0007"
Title: "Test Case: RP-PAY-0007 | PayMongo Checkout Session Initialization"
Priority: "High"
Status: "ready"
Automated: "no"
Owner: ""
Requirements: ""
Postconditions: |
  - Tested on http://localhost:3000/homepage using account testuser1@test.com (password: testuser1).
  - Cleanup: cancel unpaid gateway sessions and remove/revert any test cart or payment rows created.
  - Log out after testing when no further authenticated tests are queued.
---

# Test Case: RP-PAY-0007 | PayMongo Checkout Session Initialization

**Summary:** Verify that selected cart items create a pending payment record and redirect the user to PayMongo checkout.

**Preconditions:** User is logged in, the `/cart` page contains at least one selected in-stock artwork, and PayMongo environment keys are configured.

| # | Step Actions | Expected Results |
|---|---|---|
| 1 | Click `Proceed to Checkout (#)` in the `Order Summary` panel. | The button changes to `Processing...` and displays a loading indicator. |
| 2 | Wait for checkout initialization. | The server verifies the authenticated user, selected cart items, stock availability, item prices, and total amount. |
| 3 | Observe the result of successful initialization. | A `payments` row is created with `client_id`, primary `artist_id`, primary `artwork_id`, calculated `amount`, and `status` set to `pending`; the PayMongo checkout session receives `gcash` and `card` payment methods, PHP line items, `payment_id`, `buyer_id`, and selected cart item metadata. |
| 4 | Confirm browser navigation. | The user is redirected to the PayMongo checkout URL. If PayMongo rejects or cannot be reached, the app shows an error alert and returns the button from `Processing...` to its normal state. |

## Postconditions

- Tested on https://rotten-potato-tau.vercel.app/homepage using account testuser1@test.com (password: testuser1).
- Cleanup: cancel unpaid gateway sessions and remove/revert any test cart or payment rows created.
- Log out after testing when no further authenticated tests are queued.
