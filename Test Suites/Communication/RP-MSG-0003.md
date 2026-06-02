# Test Case: RP-MSG-0003 | Secured Alphanumeric Payload Dispatching

**Summary:** Verify that submitting text payloads appends communication segments onto active streams.

**Preconditions:** Active message chat interface is loaded with recipient node.

| # | Step Actions | Expected Results |
|---|---|---|
| 1 | Type an outbound message inside the chat entry field and hit the system send trigger. | System applies communication protocol encryptions, transfers the data packet securely, and appends the text message onto the thread display. |