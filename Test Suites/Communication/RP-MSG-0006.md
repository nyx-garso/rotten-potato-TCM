---
ID: RP-MSG-0006
Title: Test Case: RP-MSG-0006 | Remote Peer Handshake Acceptance Verification
Priority: Medium
Status: draft
Automated: no
Owner: 
Requirements: 
Postconditions: "- Tested on https://rotten-potato-tau.vercel.app/homepage using account testuser1@test.com (password: testuser1).
- Cleanup: log out after the test; remove or revert any test data created (posts, requests, payments, profile changes)
- Verify environment returned to pre-test state before running subsequent tests."
---
# Test Case: RP-MSG-0006 | Remote Peer Handshake Acceptance Verification

**Summary:** Verify that responding positively to inbound signals changes system layouts to media stream views.

**Preconditions:** Incoming calling stream signals are processing on a peer account endpoint.

| # | Step Actions | Expected Results |
|---|---|---|
| 1 | Trigger the accept handshake routine control from the targeted called account endpoint device context. | System updates screen views to display the active call page workspace, rendering data from active video and audio inputs if accessible. |

## Postconditions

- Tested on https://rotten-potato-tau.vercel.app/homepage using account testuser1@test.com (password: testuser1).
- Cleanup: log out after the test; remove or revert any test data created (posts, requests, payments, profile changes)
- Verify environment returned to pre-test state before running subsequent tests.

