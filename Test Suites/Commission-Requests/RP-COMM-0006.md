---
ID: "RP-COMM-0006"
Title: "Test Case: RP-COMM-0006 | Commissioner Hires Artist"
Priority: "High"
Status: "ready"
Automated: "no"
Owner: ""
Requirements: ""
Postconditions: |
  - Tested on https://rotten-potato-tau.vercel.app/homepage using commissioner account testuser1@test.com (password: testuser1).
  - Cleanup: remove/revert test commission request, commission offers, and related payment setup data after milestone testing is complete.
  - The accepted request should remain available for the next milestone/workspace verification pass.
---

# Test Case: RP-COMM-0006 | Commissioner Hires Artist

**Summary:** Verify that the commissioner can accept the artist's offer and move the commission into the deposit stage.

**Preconditions:** `testuser1@test.com` is logged in, the target request is `open`, and at least one incoming artist offer is visible.

| # | Step Actions | Expected Results |
|---|---|---|
| 1 | In `My Requests`, click `Hire this Artist` for the target offer. | The browser displays a confirmation prompt: `Are you sure you want to hire this artist? A deposit payment session will be created.` |
| 2 | Confirm the prompt. | The button changes to `Accepting...` while the action runs. |
| 3 | Wait for acceptance to complete. | A success modal appears with `Artist Hired!` and explains that the status is now `Awaiting Deposit`. |
| 4 | Verify the request state in `My Requests`. | The accepted offer status is updated to `accepted`, other offers for the same request are updated to `rejected`, the commission request stores the accepted `artist_id`, and the request status displays as `awaiting deposit`. |
| 5 | Observe the available next action. | The request shows a `Pay Deposit` button, leaving the accepted commission ready for the next milestone/workspace verification pass. |

## Postconditions

- Tested on https://rotten-potato-tau.vercel.app/homepage using commissioner account testuser1@test.com (password: testuser1).
- Cleanup: remove/revert test commission request, commission offers, and related payment setup data after milestone testing is complete.
- The accepted request should remain available for the next milestone/workspace verification pass.
