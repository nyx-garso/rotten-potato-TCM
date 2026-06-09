---
ID: "RP-MSG-0008"
Title: "Test Case: RP-MSG-0008 | Sidebar Modal Incoming Message Notification"
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

# Test Case: RP-MSG-0008 | Sidebar Modal Incoming Message Notification

**Summary:** Verify that when a message is received from a Top Artist sidebar conversation, the modal popup or inbox updates accordingly.

**Preconditions:** User has initiated a conversation via the Top Artist sidebar.

| # | Step Actions | Expected Results |
|---|--------------|------------------|
| 1 | Log in as `testuser1@test.com` and open a sidebar conversation with an artist. | Modal popup is visible with message thread. |
| 2 | From another account (e.g., `testuser2@test.com`), send a reply to testuser1. | Modal popup or inbox thread updates with the new message. |
| 3 | Observe the UI state. | Notification indicator appears, and the message is visible in the thread. |

## Postconditions

- Tested on https://rotten-potato-tau.vercel.app/homepage using account testuser1@test.com (password: testuser1).
- Cleanup: log out after the test; remove or revert any test data created (posts, requests, payments, profile changes)
- Verify environment returned to pre-test state before running subsequent tests.
