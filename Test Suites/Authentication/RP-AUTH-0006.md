# Test Case: RP-AUTH-0006 | Account Activation Lifecycle Completion

**Summary:** Verify that passing the validation link parameter unlocks the user account record and processes entry routing.

**Preconditions:** Automated verification email is accessible.

| # | Step Actions | Expected Results |
|---|---|---|
| 1 | Click the verification link embedded in the confirmation body text. | System switches the target profile status flag to active and redirects the viewport directly to the system homepage. |