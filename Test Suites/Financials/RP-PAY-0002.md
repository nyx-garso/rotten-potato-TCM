---
ID: "RP-PAY-0002"
Title: "Test Case: RP-PAY-0002 | Shopping Cart Page Display"
Priority: "Medium"
Status: "ready"
Automated: "no"
Owner: ""
Requirements: ""
Postconditions: |
  - Tested on http://localhost:3000/homepage using account testuser1@test.com (password: testuser1).
  - Cleanup: remove any cart items added during the test or leave the cart in its original state.
  - Log out after testing when no further authenticated tests are queued.
---

# Test Case: RP-PAY-0002 | Shopping Cart Page Display

**Summary:** Verify that the cart route displays the user's selected artworks and order summary.

**Preconditions:** User is logged in and has at least one artwork in the cart.

| # | Step Actions | Expected Results |
|---|---|---|
| 1 | From the `Added to Cart!` modal, click `View My Cart`, or navigate directly to `/cart`. | The app opens the authenticated cart page instead of redirecting to login. |
| 2 | Observe the cart page content. | The page shows `Shopping Cart`, the helper text `Review your selected masterpieces before checkout`, a `Select All` checkbox row, one or more cart item rows, and an `Order Summary` panel. |
| 3 | Review one cart item row. | The row displays a selection checkbox, artwork thumbnail, title, artist name, price, quantity controls, and a remove button. |

## Postconditions

- Tested on https://rotten-potato-tau.vercel.app/homepage using account testuser1@test.com (password: testuser1).
- Cleanup: remove any cart items added during the test or leave the cart in its original state.
- Log out after testing when no further authenticated tests are queued.
