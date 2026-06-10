---
ID: RP-PAY-0010
Title: 'Test Case: RP-PAY-0010 | Commission Deposit Paid Commit'
Priority: Medium
Status: draft
Automated: 'no'
Owner: ''
Requirements: ''
Postconditions: '- Tested on https://rotten-potato-tau.vercel.app/homepage using commissioner
  account testuser1@test.com (password: testuser1).

  - Cleanup: remove/revert test payment rows, commission status updates, and artist
  notifications after milestone testing is complete.

  - Leave the commission in `in_progress` if continuing to artist ready/final payment
  tests.

  '
Test Schedule: 2026/03/23
---


﻿---
ID: "RP-PAY-0010"
Title: "Test Case: RP-PAY-0010 | Commission Deposit Paid Commit"
Priority: "High"
Status: "ready"
Automated: "no"
Owner: ""
Requirements: ""
Postconditions: |
  - Tested on https://rotten-potato-tau.vercel.app/homepage using commissioner account testuser1@test.com (password: testuser1).
  - Cleanup: remove/revert test payment rows, commission status updates, and artist notifications after milestone testing is complete.
  - Leave the commission in `in_progress` if continuing to artist ready/final payment tests.
---

# Test Case: RP-PAY-0010 | Commission Deposit Paid Commit

**Summary:** Verify that a paid PayMongo deposit webhook commits the deposit payment and starts the commission work phase.

**Preconditions:** A commission deposit PayMongo checkout session exists with valid `payment_id`, `request_id`, `milestone_type = deposit`, and `buyer_id` metadata.

| # | Step Actions | Expected Results |
|---|---|---|
| 1 | Complete the PayMongo deposit checkout, or send a valid `checkout_session.payment.paid` webhook payload to `/api/webhooks/paymongo`. | The webhook endpoint returns `{ "received": true }` with HTTP 200. |
| 2 | Verify the matching payment record. | The `payments` row matching `payment_id` is updated to `status = paid` and receives a current `transaction_date`. |
| 3 | Verify the commission request. | The commission request matching `request_id` changes from `awaiting_deposit` to `in_progress`. |
| 4 | Verify artist notification behavior. | The accepted artist receives a `commission_payment` notification indicating that the deposit was received for the commission title and that the status is now `in progress`. |
| 5 | Open the commission workspace as the artist. | The workspace shows the artist-side action text for work in progress and displays `Mark as Ready for Review`. |

## Postconditions

- Tested on https://rotten-potato-tau.vercel.app/homepage using commissioner account testuser1@test.com (password: testuser1).
- Cleanup: remove/revert test payment rows, commission status updates, and artist notifications after milestone testing is complete.
- Leave the commission in `in_progress` if continuing to artist ready/final payment tests.
