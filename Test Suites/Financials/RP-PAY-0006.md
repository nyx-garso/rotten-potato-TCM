# Test Case: RP-PAY-0006 | Payment Ingestion Source Validation

**Summary:** Verify that selecting payment routes initiates authorization checking loops.

**Preconditions:** Integrated channel payment selectors are interactable.

| # | Step Actions | Expected Results |
|---|---|---|
| 1 | Select an explicit financial processing channel option and supply data criteria parameters. | System executes runtime checks confirming the syntax and field format validations of the financial source information. |