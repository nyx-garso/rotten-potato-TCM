---
ID: "RP-MSG-0004"
Title: "Test Case: RP-MSG-0004 | Conversation Initialization Prompt"
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

# Test Case: RP-MSG-0004 | Conversation Initialization Prompt

**Summary:** Verify that the inbox provides guidance when no conversation is selected.

**Preconditions:** Inbox page is open with no active thread.

| # | Step Actions | Expected Results |
|---|--------------|------------------|
| 1 | Open the Messages section without selecting a recipient. | System displays instructional text *“Select a friend from the list on the left to start sharing your art journey.”* |
| 2 | Observe the conversation panel. | Panel remains inactive until a recipient is chosen. |

## Postconditions

- Tested on https://rotten-potato-tau.vercel.app/homepage using account testuser1@test.com (password: testuser1).
- Cleanup: log out after the test; remove or revert any test data created (posts, requests, payments, profile changes)
- Verify environment returned to pre-test state before running subsequent tests.
