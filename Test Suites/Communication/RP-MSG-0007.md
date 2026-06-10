---
ID: RP-MSG-0007
Title: 'Test Case: RP-MSG-0007 | Inbox Incoming Message Rendering'
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


# Test Case: RP-MSG-0007 | Inbox Incoming Message Rendering

**Summary:** Verify that new inbound messages appear in the inbox conversation thread in real time.

**Preconditions:** Authenticated user session is active with inbox open.

| # | Step Actions | Expected Results |
|---|--------------|------------------|
| 1 | Log in as `testuser1@test.com`. | Inbox view is accessible. |
| 2 | From another account (e.g., `testuser2@test.com`), send a message to testuser1. | System displays the new message in the active conversation thread without requiring manual refresh. |
| 3 | Observe the conversation panel. | Message is appended chronologically, with sender identity and timestamp visible. |

## Postconditions

- Tested on https://rotten-potato-tau.vercel.app/homepage using account testuser1@test.com (password: testuser1).
- Cleanup: log out after the test; remove or revert any test data created (posts, requests, payments, profile changes)
- Verify environment returned to pre-test state before running subsequent tests.
