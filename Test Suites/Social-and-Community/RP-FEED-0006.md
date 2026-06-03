---
ID: RP-FEED-0006
Title: Test Case: RP-FEED-0006 | Asset Cross-Posting Share Workflows
Priority: Medium
Status: draft
Automated: no
Owner: 
Requirements: 
Postconditions: "- Tested on https://rotten-potato-tau.vercel.app/homepage using account testuser1@test.com (password: testuser1).
- Cleanup: log out after the test; remove or revert any test data created (posts, requests, payments, profile changes)
- Verify environment returned to pre-test state before running subsequent tests."
---
# Test Case: RP-FEED-0006 | Asset Cross-Posting Share Workflows

**Summary:** Verify that initiating content sharing maps duplicate item configurations onto user profiles.

**Preconditions:** An interactable post card is loaded inside the screen views.

| # | Step Actions | Expected Results |
|---|---|---|
| 1 | Click the share control node element button and choose the confirmation option block. | System updates user context fields, instantly creating a linked duplicate post object on the user profile marked explicitly as a shared item asset. |

## Postconditions

- Tested on https://rotten-potato-tau.vercel.app/homepage using account testuser1@test.com (password: testuser1).
- Cleanup: log out after the test; remove or revert any test data created (posts, requests, payments, profile changes)
- Verify environment returned to pre-test state before running subsequent tests.

