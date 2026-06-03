---
ID: RP-AUTH-0005
Title: Test Case: RP-AUTH-0005 | Verification Link Receipt
Priority: Medium
Status: draft
Automated: no
Owner: 
Requirements: 
Postconditions: "- Tested on https://rotten-potato-tau.vercel.app/homepage using account testuser1@test.com (password: testuser1).
- Cleanup: log out after the test; remove or revert any test data created (posts, requests, payments, profile changes)
- Verify environment returned to pre-test state before running subsequent tests."
---
# Test Case: RP-AUTH-0005 | Verification Link Receipt

**Summary:** Verify that the automated verification payload arrives accurately at the targeted destination email platform.

**Preconditions:** **[RP-AUTH-0004](Test%20Suites/Authentication/RP-AUTH-0004.md)** submission has processed completely.

| # | Step Actions | Expected Results |
|---|---|---|
| 1 | Access the third-party email account associated with the form submission data. | User receives the confirmation email containing the executable account verification hyperlink. |

## Postconditions

- Tested on https://rotten-potato-tau.vercel.app/homepage using account testuser1@test.com (password: testuser1).
- Cleanup: log out after the test; remove or revert any test data created (posts, requests, payments, profile changes)
- Verify environment returned to pre-test state before running subsequent tests.

