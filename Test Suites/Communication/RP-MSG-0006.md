---
ID: RP-MSG-0006
Title: 'Test Case: RP-MSG-0006 | Top Artist Sidebar Messaging Option'
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


# Test Case: RP-MSG-0006 | Top Artist Sidebar Messaging Option

**Summary:** Verify that clicking the messaging option in the Top Artist sidebar initializes a conversation thread with the selected artist.

**Preconditions:** Homepage is loaded with Top Artist sidebar visible.

| # | Step Actions | Expected Results |
|---|--------------|------------------|
| 1 | Locate the Top Artist sidebar on the homepage. | Sidebar displays artist profiles with messaging option. |
| 2 | Click the messaging option for a listed artist. | System opens a new conversation thread with that artist in the inbox view. |
| 3 | Observe the conversation panel. | Panel updates to show the new thread, ready for message input. |

## Postconditions

- Tested on https://rotten-potato-tau.vercel.app/homepage using account testuser1@test.com (password: testuser1).
- Cleanup: log out after the test; remove or revert any test data created (posts, requests, payments, profile changes)
- Verify environment returned to pre-test state before running subsequent tests.
