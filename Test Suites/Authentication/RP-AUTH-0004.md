---
ID: RP-AUTH-0004
Title: Test Case: RP-AUTH-0004 | Registration Trigger & Pending Account State
Priority: Medium
Status: draft
Automated: no
Owner: 
Requirements: 
Postconditions: "- Tested on https://rotten-potato-tau.vercel.app/homepage using account testuser1@test.com (password: testuser1).
- Cleanup: log out after the test; remove or revert any test data created (posts, requests, payments, profile changes)
- Verify environment returned to pre-test state before running subsequent tests."
---
# Test Case: RP-AUTH-0004 | Registration Trigger & Pending Account State

**Summary:** Verify that executing the sign-up workflow initializes the unverified database entry and sends a notification email.

**Preconditions:** Input fields contain structurally valid data configurations.

| # | Step Actions | Expected Results |
|---|---|---|
| 1 | Click the designated "Sign Up" submit button element. | System registers the baseline account object and issues a dedicated confirmation verification link to the targeted user email address. |

## Postconditions

- Tested on https://rotten-potato-tau.vercel.app/homepage using account testuser1@test.com (password: testuser1).
- Cleanup: log out after the test; remove or revert any test data created (posts, requests, payments, profile changes)
- Verify environment returned to pre-test state before running subsequent tests.

