# RP-PRF-0009 — Become a Seller (Validation & Restrictions)

**Summary:** Verify validation and restrictions during seller upgrade.  

**Preconditions:** Authenticated account with Standard Client type.

| # | Step Actions | Expected Results |
|---|--------------|------------------|
| 1 | Click “Become a Seller” without filling required fields | Error messages displayed, form not submitted |
| 2 | Attempt to upgrade with invalid data (e.g., invalid ID number) | Validation error displayed |
| 3 | Attempt to upgrade when already a Seller | “Already a Seller” message displayed, no duplicate upgrade |
