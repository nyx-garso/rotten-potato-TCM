# RP-PRF-0004 — Edit Profile (Cancel)

**Summary:** Verify that canceling edits does not change profile data.  

**Preconditions:** Authenticated account.

| # | Step Actions | Expected Results |
|---|--------------|------------------|
| 1 | Navigate to Edit Profile | Edit form loads |
| 2 | Change username/email but click Cancel | No changes saved |
| 3 | Reload profile page | Original values remain unchanged |
