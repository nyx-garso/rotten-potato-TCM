---
ID: "RP-PAY-0003"
Title: "Test Case: RP-PAY-0003 | Customer Identity and Location Ingestion"
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

# Test Case: RP-PAY-0003 | Customer Identity and Location Ingestion

**Summary:** Verify that entering textual location details populates the shipping form state fields.

**Preconditions:** The shipping data gathering view is rendered on screen.

| # | Step Actions | Expected Results |
|---|---|---|
| 1 | Input user information into the distinct text form fields (e.g., customer address name, telephone digits). | System maps the characters and updates form context state. |

## Postconditions

- Tested on https://rotten-potato-tau.vercel.app/homepage using account testuser1@test.com (password: testuser1).
- Cleanup: log out after the test; remove or revert any test data created (posts, requests, payments, profile changes)
- Verify environment returned to pre-test state before running subsequent tests.

