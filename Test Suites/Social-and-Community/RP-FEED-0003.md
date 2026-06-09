---
ID: "RP-FEED-0003"
Title: "Test Case: RP-FEED-0003 | Reaction Counter Mutators and Web Notification Dispatches"
Priority: "Medium"
Status: "draft"
Automated: "no"
Owner: ""
Requirements: ""
Postconditions: |
  - Tested on https://rotten-potato-tau.vercel.app/homepage using account testuser1@test.com (password: testuser1).
  - Cleanup: log out after the test; remove or revert any test data created (posts, requests, payments, profile changes)
  - Verify environment returned to pre-test state before running subsequent tests.
---

# Test Case: RP-FEED-0003 | Reaction Counter Mutators and Web Notification Dispatches

**Summary:** Verify that liking an asset updates interaction parameters and generates notifications for the post owner.

**Preconditions:** An artwork asset card is visible in the active feed.

| # | Step Actions | Expected Results |
|---|---|---|
| 1 | Click the heart-shaped reaction element icon component inside a loaded post card frame. | System registers a profile reaction, increments the public display calculation counter, and dispatches an automated notification alert hook to the content creator. |

## Postconditions

- Tested on https://rotten-potato-tau.vercel.app/homepage using account testuser1@test.com (password: testuser1).
- Cleanup: log out after the test; remove or revert any test data created (posts, requests, payments, profile changes)
- Verify environment returned to pre-test state before running subsequent tests.

