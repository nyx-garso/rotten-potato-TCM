---
ID: RP-MSG-0005
Title: 'Test Case: RP-MSG-0005 | Message Sending Procedure'
Priority: Medium
Status: draft
Automated: 'no'
Owner: ''
Requirements: ''
Postconditions: '- Tested on https://rotten-potato-tau.vercel.app/homepage using account
  testuser1@test.com (password: testuser1).

  - Cleanup: log out after the test; remove or revert any test data created (posts,
  requests, payments, profile changes)

  - Verify environment returned to pre-test state before running subsequent tests.

  '
Test Schedule: 2026/03/23
---


# Test Case: RP-MSG-0005 | Message Sending Procedure

**Summary:** Verify that users can send messages either through the Messages tab or via the modal popup in the Top Artist sidebar.

**Preconditions:** Authenticated user session is active.

| # | Step Actions | Expected Results |
|---|--------------|------------------|
| 1 | Navigate to the Messages tab and select a recipient. | Conversation panel opens with text input field visible. |
| 2 | Type a message into the input field and press Send. | System appends the message to the thread and confirms delivery. |
| 3 | From the homepage, locate the Top Artist sidebar and click the messaging option for a listed artist. | Modal popup opens with message input field. |
| 4 | Type a message in the modal popup and press Send. | System delivers the message to the selected artist and closes or updates the modal state. |

## Postconditions

- Tested on https://rotten-potato-tau.vercel.app/homepage using account testuser1@test.com (password: testuser1).
- Cleanup: log out after the test; remove or revert any test data created (posts, requests, payments, profile changes)
- Verify environment returned to pre-test state before running subsequent tests.
