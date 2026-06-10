---
ID: RP-COMM-0004
Title: 'Test Case: RP-COMM-0004 | Artist Sends Commission Offer'
Priority: Medium
Status: draft
Automated: 'no'
Owner: ''
Requirements: ''
Postconditions: '- Tested on https://rotten-potato-tau.vercel.app/homepage using the
  artist test account created for the commission flow.

  - Cleanup: leave the offer available until the commissioner acceptance test is complete.

  - Log out after testing when no further artist-account tests are queued.

  '
Test Schedule: 2026/03/23
---


﻿---
ID: "RP-COMM-0004"
Title: "Test Case: RP-COMM-0004 | Artist Sends Commission Offer"
Priority: "High"
Status: "ready"
Automated: "no"
Owner: ""
Requirements: ""
Postconditions: |
  - Tested on https://rotten-potato-tau.vercel.app/homepage using the artist test account created for the commission flow.
  - Cleanup: leave the offer available until the commissioner acceptance test is complete.
  - Log out after testing when no further artist-account tests are queued.
---

# Test Case: RP-COMM-0004 | Artist Sends Commission Offer

**Summary:** Verify that the artist account can submit an offer on the commission posted by `testuser1@test.com`.

**Preconditions:** Artist test account is logged in and the commissioner-created request is still `open`.

| # | Step Actions | Expected Results |
|---|---|---|
| 1 | Open `Commission` and stay on `Browse Requests`. | The board lists open requests, including the commission posted by `testuser1@test.com`. |
| 2 | Click `Send Offer` on the target request. | An inline `Submit Your Offer` form opens. |
| 3 | Enter `Your Price`, adjust the required deposit slider if needed, and enter a pitch message. | The displayed deposit percentage and calculated deposit amount update based on the entered price and slider value. |
| 4 | Click `Confirm Offer`. | The button shows `Sending...`, then a success modal appears with `Offer Submitted!`; the offer is inserted as `pending` with `request_id`, artist id, offer amount, message, and deposit percentage. |

## Postconditions

- Tested on https://rotten-potato-tau.vercel.app/homepage using the artist test account created for the commission flow.
- Cleanup: leave the offer available until the commissioner acceptance test is complete.
- Log out after testing when no further artist-account tests are queued.
