# Test Case: RP-FEED-0005 | Text Comment Injection Pipeline

**Summary:** Verify that submitting comments appends them to the card thread layout and updates metrics.

**Preconditions:** Comment text entry box contains valid string inputs.

| # | Step Actions | Expected Results |
|---|---|---|
| 1 | Write alphanumeric data into the comment input field and select the "Post" button element. | System stores the textual interaction string, appends it beneath the active media thread, and increments the aggregate thread counter by 1. |