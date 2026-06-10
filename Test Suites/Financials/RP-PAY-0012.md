---
ID: RP-PAY-0012
Title: 'Test Case: RP-PAY-0012 | Commission Final Payment Commit'
Priority: Medium
Status: draft
Automated: 'no'
Owner: ''
Requirements: ''
Postconditions: '- Tested on https://rotten-potato-tau.vercel.app/homepage and https://rotten-potato-tau.vercel.app/commissions/{request_id}
  using commissioner account testuser1@test.com (password: testuser1).

  - Cleanup: remove/revert test final-payment rows, notifications, and commission
  status changes after verification.

  - Verify the commission remains available for delivery/fulfillment testing if those
  tests are run next.

  '
Test Schedule: 2026/03/23
---


﻿---
ID: "RP-PAY-0012"
Title: "Test Case: RP-PAY-0012 | Commission Final Payment Commit"
Priority: "High"
Status: "ready"
Automated: "no"
Owner: ""
Requirements: ""
Postconditions: |
  - Tested on https://rotten-potato-tau.vercel.app/homepage and https://rotten-potato-tau.vercel.app/commissions/{request_id} using commissioner account testuser1@test.com (password: testuser1).
  - Cleanup: remove/revert test final-payment rows, notifications, and commission status changes after verification.
  - Verify the commission remains available for delivery/fulfillment testing if those tests are run next.
---

# Test Case: RP-PAY-0012 | Commission Final Payment Commit

**Summary:** Verify that the commissioner can pay the remaining commission balance and that the paid webhook completes the financial milestone.

**Preconditions:** The commission status is `awaiting_final_payment`, the accepted offer has a known amount and deposit percentage, and PayMongo environment keys are configured.

| # | Step Actions | Expected Results |
|---|---|---|
| 1 | Log in as `testuser1@test.com` and open the accepted commission from `My Requests` or `/commissions/{request_id}`. | The commission displays `awaiting final payment` and shows `Pay Balance (₱amount)` or `Pay Remaining Balance`. |
| 2 | Click the final payment action. | The UI enters a processing state while the final payment session is created. |
| 3 | Verify checkout initialization. | A `payments` row is created with `request_id`, accepted `artist_id`, final balance `amount`, `milestone_type = final`, and `status = pending`; the PayMongo metadata contains `payment_id`, `request_id`, `milestone_type = final`, and `buyer_id`. |
| 4 | Complete the PayMongo final checkout, or send a valid `checkout_session.payment.paid` webhook payload. | The webhook marks the final payment row as `paid` and sets `transaction_date`. |
| 5 | Verify commission completion state. | The commission request status becomes `completed`, `shipping_status` becomes `pending_shipment`, and the artist receives a `commission_payment` notification for the final payment. |
| 6 | Review the artist dashboard or workspace. | The completed commission payment is included in the artist's paid payment records, and the workspace shows the project as successfully completed and funded. |

## Postconditions

- Tested on https://rotten-potato-tau.vercel.app/homepage and https://rotten-potato-tau.vercel.app/commissions/{request_id} using commissioner account testuser1@test.com (password: testuser1).
- Cleanup: remove/revert test final-payment rows, notifications, and commission status changes after verification.
- Verify the commission remains available for delivery/fulfillment testing if those tests are run next.
