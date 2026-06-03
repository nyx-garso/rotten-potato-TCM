---
ID: RP-MSG-0005
Title: Test Case: RP-MSG-0005 | RTC Communication Pipeline Signaling Requests
Priority: Medium
Status: draft
Automated: no
Owner: 
Requirements: 
Postconditions: "- Tested on https://rotten-potato-tau.vercel.app/homepage using account testuser1@test.com (password: testuser1).
- Cleanup: log out after the test; remove or revert any test data created (posts, requests, payments, profile changes)
- Verify environment returned to pre-test state before running subsequent tests."
---
# Test Case: RP-MSG-0005 | RTC Communication Pipeline Signaling Requests

**Summary:** Verify that launching hardware calling routines attempts network requests to peer accounts.

**Preconditions:** Peer recipient node session context is active.

| # | Step Actions | Expected Results |
|---|---|---|
| 1 | Select either the audio microphone button or the video camera hardware connection controller in the chat toolbar. | System tests local driver availability and begins sending network real-time communication connection signal request packets to the targeted remote user account. |

## Postconditions

- Tested on https://rotten-potato-tau.vercel.app/homepage using account testuser1@test.com (password: testuser1).
- Cleanup: log out after the test; remove or revert any test data created (posts, requests, payments, profile changes)
- Verify environment returned to pre-test state before running subsequent tests.

