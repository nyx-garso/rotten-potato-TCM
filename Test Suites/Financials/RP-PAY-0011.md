---
ID: "RP-PAY-0011"
Title: "Test Case: RP-PAY-0011 | Artist Marks Commission Ready for Final Payment"
Priority: "Medium"
Status: "ready"
Automated: "no"
Owner: ""
Requirements: ""
Postconditions: |
  - Tested on https://rotten-potato-tau.vercel.app/commissions/{request_id} using the accepted artist test account.
  - Cleanup: restore the commission status if the final payment test will not be run.
  - Leave the commission in `awaiting_final_payment` when continuing to final payment verification.
---

# Test Case: RP-PAY-0011 | Artist Marks Commission Ready for Final Payment

**Summary:** Verify that the artist can advance an in-progress commission to the final-payment stage after accepting and working on the commission.

**Preconditions:** Artist test account is logged in, the commission deposit has been paid, and the commission status is `in_progress`.

| # | Step Actions | Expected Results |
|---|---|---|
| 1 | Open the accepted commission workspace at `/commissions/{request_id}` as the artist. | The workspace loads `Project Milestones`, displays status `in progress`, and shows the artist action `Mark as Ready for Review`. |
| 2 | Click `Mark as Ready for Review`. | The button changes to `Updating...` while the status update is processed. |
| 3 | Wait for the workspace to reload. | The commission request status changes to `awaiting_final_payment`. |
| 4 | Review the workspace as the artist. | The artist sees `Awaiting final balance from the client...`; no artist-side payment button is shown. |
| 5 | Review the commission as the commissioner. | The commissioner sees a `Pay Balance (₱amount)` or `Pay Remaining Balance` action based on the accepted offer amount minus the deposit amount. |

## Postconditions

- Tested on https://rotten-potato-tau.vercel.app/commissions/{request_id} using the accepted artist test account.
- Cleanup: restore the commission status if the final payment test will not be run.
- Leave the commission in `awaiting_final_payment` when continuing to final payment verification.
