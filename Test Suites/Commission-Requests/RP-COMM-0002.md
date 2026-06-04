---
ID: "RP-COMM-0002"
Title: "Test Case: RP-COMM-0002 | Commissioner Posts Open Request"
Priority: "High"
Status: "ready"
Automated: "no"
Owner: ""
Requirements: ""
Postconditions: |
  - Tested on https://rotten-potato-tau.vercel.app/homepage using commissioner account testuser1@test.com (password: testuser1).
  - Cleanup: remove or mark closed the test commission request after the dependent artist-offer tests finish.
  - Log out after testing when no further authenticated tests are queued.
---

# Test Case: RP-COMM-0002 | Commissioner Posts Open Request

**Summary:** Verify that `testuser1@test.com` can create an open commission request that appears on the board.

**Preconditions:** User is logged in as `testuser1@test.com` and the `Post a Request` modal is open.

| # | Step Actions | Expected Results |
|---|---|---|
| 1 | Enter a project title, detailed description, numeric budget, and future deadline. | The form accepts the entered request data. |
| 2 | Click `Post Commission`. | The button changes to `Posting...` while the request is being saved. |
| 3 | Wait for submission to complete. | A success modal appears with `Request Posted!` and explains that artists can submit offers. |
| 4 | Dismiss the success modal and open `My Requests`. | The newly created request appears for the commissioner with `status` shown as `open`; if no offers exist yet, the page displays `No offers received yet. Artists will see this on the job board!`. |

## Postconditions

- Tested on https://rotten-potato-tau.vercel.app/homepage using commissioner account testuser1@test.com (password: testuser1).
- Cleanup: remove or mark closed the test commission request after the dependent artist-offer tests finish.
- Log out after testing when no further authenticated tests are queued.
