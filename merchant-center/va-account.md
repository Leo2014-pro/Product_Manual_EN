# VA Account

The VA module is the core operations desk for merchants to manage the full lifecycle of virtual accounts, covering user creation and verification, sub-account opening and management, transaction data querying and exporting, as well as complete operation trails and audit tracking.

## User Management

**Feature Description**: View end-user information associated with VA, supporting new user creation.

**Operations**:
- Filter: View all VA-associated users, supporting search by name, phone number, and email.
- Add: Select enterprise/individual, fill in basic information and submit; a user ID is generated and can be used to associate with VA accounts subsequently.

---

## Account Management

**Feature Description**: Display all VA sub-account information under the current merchant, supporting the creation of new sub-accounts.

**Operations**:
- Filter: Support filtering by account status, type, and other criteria.
- Add: Select account type, bind user, and submit. Some account types require the user to complete verification before activation.

---

## Transaction Inquiry

**Feature Description**: Aggregate and display all transaction data across all VA accounts under the current merchant, supporting filtering and export.

**Operations**:
- Filter: Query transaction records by order number, transaction type, transaction status, time range, and other criteria.
- View: Single transaction details (including counterparty, fees, processing timeline).

---

## User Verification Records

**Feature Description**: Display KYC/KYB verification history and current status for all users, used to track verification progress.

**Operations**:
- Filter: Filter by user or verification status; click to view submitted materials and review comments.

---

## Account Creation Records

**Feature Description**: Aggregate and display the creation history of all VA sub-accounts, including creation source, operator, and status, used for operation trails and root cause analysis.

**Operations**:
- Filter: View all account creation records in reverse chronological order, supporting filtering by account number, user, and creation source (manual/API); click to view creation details.
