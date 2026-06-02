# Test Case: RP-FEED-0003 | Reaction Counter Mutators and Web Notification Dispatches

**Summary:** Verify that liking an asset updates interaction parameters and generates notifications for the post owner.

**Preconditions:** An artwork asset card is visible in the active feed.

| # | Step Actions | Expected Results |
|---|---|---|
| 1 | Click the heart-shaped reaction element icon component inside a loaded post card frame. | System registers a profile reaction, increments the public display calculation counter, and dispatches an automated notification alert hook to the content creator. |