---
ID: "RP-PAY-0001"
Title: "Test Case: RP-PAY-0001 | Marketplace Add to Cart"
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

# Test Case: RP-PAY-0001 | Marketplace Add to Cart

**Summary:** Verify that an available artwork can be added to the authenticated user's shopping cart from the Browse Artworks page.

**Preconditions:** User is logged in and the Browse Artworks tab displays at least one available, in-stock artwork that is not owned by the user.

| # | Step Actions | Expected Results |
|---|---|---|
| 1 | Navigate to `Homepage` and open the Browse Artworks view if it is not already active. | The page displays the `Browse Artworks` heading, search/filter controls, and artwork cards with prices and `Add to Cart` buttons. |
| 2 | Click `Add to Cart` on an available artwork. | The clicked button shows an `Adding...` loading state while the cart update is processed. |
| 3 | Wait for the add-to-cart action to complete. | A modal appears with `Added to Cart!`, the selected artwork title, `View My Cart`, and `Continue Shopping`. |

## Postconditions

- Tested on https://rotten-potato-tau.vercel.app/homepage using account testuser1@test.com (password: testuser1).
- Cleanup: remove any cart items added during the test or leave the cart in its original state.
- Log out after testing when no further authenticated tests are queued.
