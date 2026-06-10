---
ID: RP-COMM-0003
Title: 'Test Case: RP-COMM-0003 | Artist Test Account Setup'
Priority: Medium
Status: draft
Automated: 'no'
Owner: ''
Requirements: ''
Postconditions: '- Tested on https://rotten-potato-tau.vercel.app/signup and https://rotten-potato-tau.vercel.app/onboarding/artist
  using a new artist test account.

  - Cleanup: record the artist test account email used for later teardown.

  - Log out after artist setup if switching back to the commissioner account.

  '
Test Schedule: 2026/03/23
---


﻿---
ID: "RP-COMM-0003"
Title: "Test Case: RP-COMM-0003 | Artist Test Account Setup"
Priority: "High"
Status: "ready"
Automated: "no"
Owner: ""
Requirements: ""
Postconditions: |
  - Tested on https://rotten-potato-tau.vercel.app/signup and https://rotten-potato-tau.vercel.app/onboarding/artist using a new artist test account.
  - Cleanup: record the artist test account email used for later teardown.
  - Log out after artist setup if switching back to the commissioner account.
---

# Test Case: RP-COMM-0003 | Artist Test Account Setup

**Summary:** Verify that a newly created account can be converted into an artist account before accepting commission work.

**Preconditions:** A commission request already exists from `testuser1@test.com`; use a unique new test email for the artist account.

| # | Step Actions | Expected Results |
|---|---|---|
| 1 | Navigate to `/signup` and create a new account with full name, unique email, and password. Select `I want to Buy Art` if the account should be converted through onboarding, or `I want to Sell Art` if direct artist signup is being tested. | The account is created and the app redirects to `/login` with the account-created message. |
| 2 | Log in with the new account. | The app opens the authenticated homepage. |
| 3 | If the account is not already an artist, open the profile menu and click `Become an Artist`, or navigate to `/onboarding/artist`. | The `GamâLokal Artist Setup` page displays `Specialty`, `Location (Barangay)`, `Price Range`, and `Complete Studio Setup`. |
| 4 | Complete the artist setup form and submit. | The app creates or updates the artist profile, updates the user role to `artist`, and redirects to `/dashboard`. |

## Postconditions

- Tested on https://rotten-potato-tau.vercel.app/signup and https://rotten-potato-tau.vercel.app/onboarding/artist using a new artist test account.
- Cleanup: record the artist test account email used for later teardown.
- Log out after artist setup if switching back to the commissioner account.
