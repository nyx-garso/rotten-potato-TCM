# Test Case: RP-MSG-0008 | Inbox Conversation Search Handling

**Summary:** Verify that inbox search input accepts text and updates the visible conversation results state.

**Preconditions:** Inbox page is open and the search box is enabled.

| # | Step Actions | Expected Results |
|---|---|---|
| 1 | Type a valid contact name or conversation keyword into the inbox search field. | System accepts the query and updates the conversation results state based on the entered term. |
| 2 | Submit a query that returns no matching conversations. | System shows a no-results state without breaking the inbox layout. |
