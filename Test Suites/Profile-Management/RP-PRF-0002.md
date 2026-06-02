# RP-PRF-0002 — Profile Display (Edge Cases)

**Summary:** Validate handling of long usernames and unusual characters.  

**Preconditions:** Authenticated account with modified profile data.

| # | Step Actions | Expected Results |
|---|--------------|------------------|
| 1 | Log in with account containing long username | Username is truncated or wrapped correctly |
| 2 | Log in with account containing special characters | Special characters render correctly without breaking layout |
