---
ID: RP-COMM-0005
Title: 'Test Case: RP-COMM-0005 | Commissioner Reviews Incoming Offers'
Priority: Medium
Status: draft
Automated: 'no'
Owner: ''
Requirements: ''
Postconditions: '- Tested on https://rotten-potato-tau.vercel.app/homepage using commissioner
  account testuser1@test.com (password: testuser1).

  - Cleanup: keep the request and offer intact until RP-COMM-0006 is complete.

  - Log out after testing when no further authenticated tests are queued.

  '
Test Schedule: 2026/03/23
---


﻿---
ID: "RP-COMM-0005"
Title: "Test Case: RP-COMM-0005 | Commissioner Reviews Incoming Offers"
Priority: "Medium"
Status: "ready"
Automated: "no"
Owner: ""
Requirements: ""
Postconditions: |
  - Tested on https://rotten-potato-tau.vercel.app/homepage using commissioner account testuser1@test.com (password: testuser1).
  - Cleanup: keep the request and offer intact until RP-COMM-0006 is complete.
  - Log out after testing when no further authenticated tests are queued.
---

# Test Case: RP-COMM-0005 | Commissioner Reviews Incoming Offers

**Summary:** Verify that the commissioner can see the artist's incoming offer on their own commission request.

**Preconditions:** Artist test account has submitted an offer on the commission created by `testuser1@test.com`.

| # | Step Actions | Expected Results |
|---|---|---|
| 1 | Log in as `testuser1@test.com` and open the `Commission` tab. | The `Commission Board` page loads for the commissioner. |
| 2 | Click `My Requests`. | The commissioner's request list displays the posted request with `status` shown as `open`. |
| 3 | Locate the target request's `Incoming Offers` section. | The artist offer appears with artist name, offered amount, message, and a `Hire this Artist` button. |

## Postconditions

- Tested on https://rotten-potato-tau.vercel.app/homepage using commissioner account testuser1@test.com (password: testuser1).
- Cleanup: keep the request and offer intact until RP-COMM-0006 is complete.
- Log out after testing when no further authenticated tests are queued.
