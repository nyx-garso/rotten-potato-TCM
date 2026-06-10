---
ID: RP-PAY-0009
Title: 'Test Case: RP-PAY-0009 | Commission Deposit Checkout Initialization'
Priority: Medium
Status: draft
Automated: 'no'
Owner: ''
Requirements: ''
Postconditions: '- Tested on https://rotten-potato-tau.vercel.app/homepage using commissioner
  account testuser1@test.com (password: testuser1).

  - Cleanup: cancel unpaid gateway sessions and remove/revert test payment rows if
  the deposit checkout is not completed.

  - Keep the accepted commission available for milestone/workspace tests when continuing
  the suite.

  '
Test Schedule: 2026/03/23
---


﻿---
ID: "RP-PAY-0009"
Title: "Test Case: RP-PAY-0009 | Commission Deposit Checkout Initialization"
Priority: "High"
Status: "ready"
Automated: "no"
Owner: ""
Requirements: ""
Postconditions: |
  - Tested on https://rotten-potato-tau.vercel.app/homepage using commissioner account testuser1@test.com (password: testuser1).
  - Cleanup: cancel unpaid gateway sessions and remove/revert test payment rows if the deposit checkout is not completed.
  - Keep the accepted commission available for milestone/workspace tests when continuing the suite.
---

# Test Case: RP-PAY-0009 | Commission Deposit Checkout Initialization

**Summary:** Verify that hiring an artist on a commission exposes the deposit payment action and initializes a PayMongo checkout session for the deposit amount.

**Preconditions:** `testuser1@test.com` has accepted an artist offer for a commission request, and the request status is `awaiting_deposit`.

| # | Step Actions | Expected Results |
|---|---|---|
| 1 | Log in as `testuser1@test.com`, open `Commission`, and go to `My Requests`. | The accepted commission appears with status `awaiting deposit` and a `Pay Deposit` action. |
| 2 | Click `Pay Deposit` from `My Requests`, or open the commission workspace and click `Pay Deposit (₱amount)`. | The UI changes to a processing state (`Redirecting...` or `Processing...`). |
| 3 | Wait for checkout initialization. | The system creates a `payments` row with `client_id`, accepted `artist_id`, `request_id`, calculated deposit `amount`, `milestone_type = deposit`, and `status = pending`. |
| 4 | Confirm the PayMongo session payload. | The checkout session uses PHP currency, `gcash` and `card` payment options, a `Commission Deposit - <title>` line item, and metadata containing `payment_id`, `request_id`, `milestone_type = deposit`, and `buyer_id`. |
| 5 | Observe browser navigation. | The user is redirected to the PayMongo checkout URL; if the gateway fails, the app shows a payment initialization error and exits the processing state. |

## Postconditions

- Tested on https://rotten-potato-tau.vercel.app/homepage using commissioner account testuser1@test.com (password: testuser1).
- Cleanup: cancel unpaid gateway sessions and remove/revert test payment rows if the deposit checkout is not completed.
- Keep the accepted commission available for milestone/workspace tests when continuing the suite.
