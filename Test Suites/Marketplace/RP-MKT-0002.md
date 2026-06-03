---
ID: RP-MKT-0002
Title: Test Case: RP-MKT-0002 | Artwork Price and Buy Control Visibility
Priority: Medium
Status: draft
Automated: no
Owner: 
Requirements: 
Postconditions: "- Tested on https://rotten-potato-tau.vercel.app/homepage using account testuser1@test.com (password: testuser1).
- Cleanup: log out after the test; remove or revert any test data created (posts, requests, payments, profile changes)
- Verify environment returned to pre-test state before running subsequent tests."
---
# Test Case: RP-MKT-0002 | Artwork Price and Buy Control Visibility

**Summary:** Verify that marketplace artwork cards display the price and Buy control in the live release.

**Preconditions:** Authenticated user session is available and the Marketplace catalog is loaded.

| # | Step Actions | Expected Results |
|---|---|---|
| 1 | Open the Marketplace view from the main navigation. | System renders artwork cards with visible price metadata and a Buy control. |

## Postconditions

- Tested on https://rotten-potato-tau.vercel.app/homepage using account testuser1@test.com (password: testuser1).
- Cleanup: log out after the test; remove or revert any test data created (posts, requests, payments, profile changes)
- Verify environment returned to pre-test state before running subsequent tests.

