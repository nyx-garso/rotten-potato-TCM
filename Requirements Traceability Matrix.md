# Requirements Traceability Matrix (RTM) - Rotten Potato (RP.010.001)

| Requirement ID | Module | Description | Linked Test Cases |
| :--- | :--- | :--- | :--- |
| **AUTH-01** | Authentication | Account Sign Up and Registration Form | **[RP-AUTH-0001](Test%20Suites/Authentication/RP-AUTH-0001.md)**, **[RP-AUTH-0002](Test%20Suites/Authentication/RP-AUTH-0002.md)** |
| **AUTH-02** | Authentication | Form Fields Input and Validation Constraints | **[RP-AUTH-0003](Test%20Suites/Authentication/RP-AUTH-0003.md)**, **[RP-AUTH-0004](Test%20Suites/Authentication/RP-AUTH-0004.md)** |
| **AUTH-03** | Authentication | Account Lifecycle Activation via Email Verification | **[RP-AUTH-0005](Test%20Suites/Authentication/RP-AUTH-0005.md)**, **[RP-AUTH-0006](Test%20Suites/Authentication/RP-AUTH-0006.md)** |
| **PRF-01** | Profile Management | Profile Display (username, email, account type, join date) | **[RP-PRF-0001](Test%20Suites/Profile-Management/RP-PRF-0001.md)**, **[RP-PRF-0002](Test%20Suites/Profile-Management/RP-PRF-0002.md)** |
| **PRF-02** | Profile Management | Edit Profile (update username/email, cancel edits) | **[RP-PRF-0003](Test%20Suites/Profile-Management/RP-PRF-0003.md)**, **[RP-PRF-0004](Test%20Suites/Profile-Management/RP-PRF-0004.md)** |
| **PRF-03** | Profile Management | Account Type Handling (Standard Client vs Seller options) | **[RP-PRF-0005](Test%20Suites/Profile-Management/RP-PRF-0005.md)** |
| **PRF-04** | Profile Management | Recent Activity Logging (saved items, commissions, purchases) | **[RP-PRF-0006](Test%20Suites/Profile-Management/RP-PRF-0006.md)**, **[RP-PRF-0007](Test%20Suites/Profile-Management/RP-PRF-0007.md)** |
| **PRF-05** | Profile Management | Become a Seller (upgrade account type, unlock seller options) | **[RP-PRF-0008](Test%20Suites/Profile-Management/RP-PRF-0008.md)**, **[RP-PRF-0009](Test%20Suites/Profile-Management/RP-PRF-0009.md)** |
| **SRCH-01** | Discovery and Navigation | Global Text Search Execution Engine | **[RP-SRCH-0001](Test%20Suites/Discovery-and-Navigation/RP-SRCH-0001.md)** |
| **SRCH-02** | Discovery and Navigation | Dynamic Filter Tags Processing | **[RP-SRCH-0002](Test%20Suites/Discovery-and-Navigation/RP-SRCH-0002.md)** |
| **SRCH-03** | Discovery and Navigation | Interactive Result Cards (Hover and Selection Views) | **[RP-SRCH-0003](Test%20Suites/Discovery-and-Navigation/RP-SRCH-0003.md)**, **[RP-SRCH-0004](Test%20Suites/Discovery-and-Navigation/RP-SRCH-0004.md)** |
| **MKT-01** | Marketplace | Art Catalog Browsing, Search, Filter, and Sort Controls | **[RP-MKT-0001](Test%20Suites/Marketplace/RP-MKT-0001.md)**, **[RP-MKT-0002](Test%20Suites/Marketplace/RP-MKT-0002.md)** |
| **MKT-02** | Marketplace | Artwork Price and Buy Control Visibility | **[RP-MKT-0002](Test%20Suites/Marketplace/RP-MKT-0002.md)** |
| **MKT-03** | Marketplace | Ask Artist Control Availability and Browse Stability | **[RP-MKT-0003](Test%20Suites/Marketplace/RP-MKT-0003.md)** |
| **PAY-01** | Financials | Marketplace Add-to-Cart and Shopping Cart Display | **[RP-PAY-0001](Test%20Suites/Financials/RP-PAY-0001.md)**, **[RP-PAY-0002](Test%20Suites/Financials/RP-PAY-0002.md)** |
| **PAY-02** | Financials | Selective Checkout, Quantity Updates, and Cart Cleanup Controls | **[RP-PAY-0003](Test%20Suites/Financials/RP-PAY-0003.md)**, **[RP-PAY-0004](Test%20Suites/Financials/RP-PAY-0004.md)**, **[RP-PAY-0005](Test%20Suites/Financials/RP-PAY-0005.md)**, **[RP-PAY-0006](Test%20Suites/Financials/RP-PAY-0006.md)** |
| **PAY-03** | Financials | PayMongo Checkout Session and Paid Webhook Commit Flow | **[RP-PAY-0007](Test%20Suites/Financials/RP-PAY-0007.md)**, **[RP-PAY-0008](Test%20Suites/Financials/RP-PAY-0008.md)** |
| **PAY-04** | Financials | Commission Deposit Payment Initialization and Paid Commit | **[RP-PAY-0009](Test%20Suites/Financials/RP-PAY-0009.md)**, **[RP-PAY-0010](Test%20Suites/Financials/RP-PAY-0010.md)** |
| **PAY-05** | Financials | Artist Ready-for-Final-Payment Gate and Commission Final Payment Commit | **[RP-PAY-0011](Test%20Suites/Financials/RP-PAY-0011.md)**, **[RP-PAY-0012](Test%20Suites/Financials/RP-PAY-0012.md)** |
| **FEED-01** | Social-and-Community | Artwork Publication and Timeline Injection | **[RP-FEED-0001](Test%20Suites/Social-and-Community/RP-FEED-0001.md)**, **[RP-FEED-0002](Test%20Suites/Social-and-Community/RP-FEED-0002.md)** |
| **FEED-02** | Social-and-Community | Reaction Handlers and Targeted System Notifications | **[RP-FEED-0003](Test%20Suites/Social-and-Community/RP-FEED-0003.md)** |
| **FEED-03** | Social-and-Community | Core Social Interaction Hooks (Comments & Shares) | **[RP-FEED-0004](Test%20Suites/Social-and-Community/RP-FEED-0004.md)**, **[RP-FEED-0005](Test%20Suites/Social-and-Community/RP-FEED-0005.md)**, **[RP-FEED-0006](Test%20Suites/Social-and-Community/RP-FEED-0006.md)** |
| **MSG-01**     | Communication | Inbox Empty State Rendering | **[RP-MSG-0001](Test%20Suites/Communication/RP-MSG-0001.md)** |
| **MSG-02**     | Communication | Inbox Search & Conversation Thread Restorations | **[RP-MSG-0002](Test%20Suites/Communication/RP-MSG-0002.md)**, **[RP-MSG-0008](Test%20Suites/Communication/RP-MSG-0008.md)** |
| **MSG-03**     | Communication | Conversation Initialization Prompt | **[RP-MSG-0003](Test%20Suites/Communication/RP-MSG-0003.md)** |
| **MSG-04**     | Communication | Message Sending Procedure | **[RP-MSG-0004](Test%20Suites/Communication/RP-MSG-0004.md)** |
| **MSG-05**     | Communication | Top Artist Sidebar Messaging Option | **[RP-MSG-0005](Test%20Suites/Communication/RP-MSG-0005.md)** |
| **MSG-06**     | Communication | Receiving Messages (Inbox & Sidebar Modal) | **[RP-MSG-0006](Test%20Suites/Communication/RP-MSG-0006.md)**, **[RP-MSG-0007](Test%20Suites/Communication/RP-MSG-0007.md)** |
| **COMM-01** | Commission-Requests | Commissioner Request Creation and Open Request Listing | **[RP-COMM-0001](Test%20Suites/Commission-Requests/RP-COMM-0001.md)**, **[RP-COMM-0002](Test%20Suites/Commission-Requests/RP-COMM-0002.md)** |
| **COMM-02** | Commission-Requests | Artist Account Setup and Offer Submission | **[RP-COMM-0003](Test%20Suites/Commission-Requests/RP-COMM-0003.md)**, **[RP-COMM-0004](Test%20Suites/Commission-Requests/RP-COMM-0004.md)** |
| **COMM-03** | Commission-Requests | Commissioner Offer Review, Artist Hiring, and Deposit-Ready State | **[RP-COMM-0005](Test%20Suites/Commission-Requests/RP-COMM-0005.md)**, **[RP-COMM-0006](Test%20Suites/Commission-Requests/RP-COMM-0006.md)** |
| **REV-01** | Reputation | Artwork Rating Score and Count Visibility | **[RP-REV-0001](Test%20Suites/Reputation/RP-REV-0001.md)**, **[RP-REV-0002](Test%20Suites/Reputation/RP-REV-0002.md)**, **[RP-REV-0003](Test%20Suites/Reputation/RP-REV-0003.md)** |
| **REV-02** | Reputation | Rating Metadata Stability Across Browse States | **[RP-REV-0004](Test%20Suites/Reputation/RP-REV-0004.md)**, **[RP-REV-0005](Test%20Suites/Reputation/RP-REV-0005.md)** |
