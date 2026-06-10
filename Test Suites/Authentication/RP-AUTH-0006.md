---
ID: RP-AUTH-0006
Title: 'Test Case: RP-AUTH-0006 | Account Activation Lifecycle Completion'
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


# Test Case: RP-AUTH-0006 | Account Activation Lifecycle Completion

**Summary:** Verify that passing the validation link parameter unlocks the user account record and processes entry routing.

**Preconditions:** Automated verification email is accessible.

| # | Step Actions | Expected Results |
|---|---|---|
| 1 | Click the verification link embedded in the confirmation body text. | System switches the target profile status flag to active and redirects the viewport directly to the system homepage. |

## Postconditions

- Tested on https://rotten-potato-tau.vercel.app/homepage using account testuser1@test.com (password: testuser1).
- Cleanup: log out after the test; remove or revert any test data created (posts, requests, payments, profile changes)
- Verify environment returned to pre-test state before running subsequent tests.

