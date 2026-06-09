---
ID: "RP-COMM-0001"
Title: "Test Case: RP-COMM-0001 | Commissioner Opens Post Request Modal"
Priority: "Medium"
Status: "ready"
Automated: "no"
Owner: ""
Requirements: ""
Postconditions: |
  - Tested on https://rotten-potato-tau.vercel.app/homepage using commissioner account testuser1@test.com (password: testuser1).
  - Cleanup: close the modal if no request is posted.
  - Log out after testing when no further authenticated tests are queued.
---

# Test Case: RP-COMM-0001 | Commissioner Opens Post Request Modal

**Summary:** Verify that the authenticated commissioner can open the live commission request creation modal.

**Preconditions:** User is logged in as `testuser1@test.com` and is on `https://rotten-potato-tau.vercel.app/homepage`.

| # | Step Actions | Expected Results |
|---|---|---|
| 1 | Click the `Commission` navigation tab. | The `Commission Board` page displays with `Browse Requests`, `My Requests`, and `Post Commission Request`. |
| 2 | Click `Post Commission Request`. | The `Post a Request` modal opens. |
| 3 | Observe the modal fields. | The modal contains `Project Title`, `Detailed Description`, `Budget`, `Deadline`, a close control, and the `Post Commission` submit button. |

## Postconditions

- Tested on https://rotten-potato-tau.vercel.app/homepage using commissioner account testuser1@test.com (password: testuser1).
- Cleanup: close the modal if no request is posted.
- Log out after testing when no further authenticated tests are queued.
