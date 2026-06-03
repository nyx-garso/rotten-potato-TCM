---
ID: RP-FEED-0005
Title: Test Case: RP-FEED-0005 | Text Comment Injection Pipeline
Priority: Medium
Status: draft
Automated: no
Owner: 
Requirements: 
Postconditions: "- Tested on https://rotten-potato-tau.vercel.app/homepage using account testuser1@test.com (password: testuser1).
- Cleanup: log out after the test; remove or revert any test data created (posts, requests, payments, profile changes)
- Verify environment returned to pre-test state before running subsequent tests."
---
# Test Case: RP-FEED-0005 | Text Comment Injection Pipeline

**Summary:** Verify that submitting comments appends them to the card thread layout and updates metrics.

**Preconditions:** Comment text entry box contains valid string inputs.

| # | Step Actions | Expected Results |
|---|---|---|
| 1 | Write alphanumeric data into the comment input field and select the "Post" button element. | System stores the textual interaction string, appends it beneath the active media thread, and increments the aggregate thread counter by 1. |

## Postconditions

- Tested on https://rotten-potato-tau.vercel.app/homepage using account testuser1@test.com (password: testuser1).
- Cleanup: log out after the test; remove or revert any test data created (posts, requests, payments, profile changes)
- Verify environment returned to pre-test state before running subsequent tests.

