---
ID: "RP-AUTH-0002"
Title: "Test Case: RP-AUTH-0002 | Sign Up Fields Form Presentation"
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

# Test Case: RP-AUTH-0002 | Sign Up Fields Form Presentation

**Summary:** Verify that the displayed registration form explicitly features structural data input fields.

**Preconditions:** User has executed **[RP-AUTH-0001](Test%20Suites/Authentication/RP-AUTH-0001.md)** successfully.

| # | Step Actions | Expected Results |
|---|---|---|
| 1 | Audit the visual interface elements of the active sign up view. | Verify that distinct input fields are visible for Email, Username, and Password. |

## Postconditions

- Tested on https://rotten-potato-tau.vercel.app/homepage using account testuser1@test.com (password: testuser1).
- Cleanup: log out after the test; remove or revert any test data created (posts, requests, payments, profile changes)
- Verify environment returned to pre-test state before running subsequent tests.

