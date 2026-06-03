---
ID: RP-PRF-0002
Title: RP-PRF-0002 — Profile Display (Edge Cases)
Priority: Medium
Status: draft
Automated: no
Owner: 
Requirements: 
Postconditions: "- Tested on https://rotten-potato-tau.vercel.app/homepage using account testuser1@test.com (password: testuser1).
- Cleanup: log out after the test; remove or revert any test data created (posts, requests, payments, profile changes)
- Verify environment returned to pre-test state before running subsequent tests."
---
# RP-PRF-0002 — Profile Display (Edge Cases)

**Summary:** Validate handling of long usernames and unusual characters.  

**Preconditions:** Authenticated account with modified profile data.

| # | Step Actions | Expected Results |
|---|--------------|------------------|
| 1 | Log in with account containing long username | Username is truncated or wrapped correctly |
| 2 | Log in with account containing special characters | Special characters render correctly without breaking layout |

## Postconditions

- Tested on https://rotten-potato-tau.vercel.app/homepage using account testuser1@test.com (password: testuser1).
- Cleanup: log out after the test; remove or revert any test data created (posts, requests, payments, profile changes)
- Verify environment returned to pre-test state before running subsequent tests.

