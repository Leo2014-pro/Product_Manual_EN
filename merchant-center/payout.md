# Payout

Payout is the core functional module for merchants to manage all **outbound payment** (paying users) orders and track fund status.

## Crypto Payout Orders

**Feature Description**: This page centrally displays your digital currency payout order records for easy querying, tracking, and management.

**Operations**:
- Filter: Search by order number, type, transaction status, and time.
- View: Detailed fields of the order's withdrawal.
  - Order Status: After the platform submits and the on-chain confirmation is successful, the order transitions to "Processing".
  - Callback Notification: After a successful callback, it indicates that the downstream interface has been notified.
- Auto-Approval Settings: You can configure which currencies require manual review in the merchant backend. If not configured, all are auto-approved.
  - List: Displays auto-approval data for configured currencies.
  - Auto-Approval Threshold: Withdrawal orders above this amount require manual merchant review.
  - Currency: The currency requiring review.
  - Chain Type: The public chain to which the currency belongs.
  - Status: Enabled, Disabled.

- Batch Payout: Download the template to fill in batch payout receiving information.
- Review / Batch Review: After approval, the payout order proceeds to on-chain payment. Rejected orders will fail.
- Switch Status: This operation only exists in the sandbox environment and is used for debugging during API integration.

---

## Fiat Payout Orders

**Feature Description**: This page centrally displays your fiat currency payout order records for easy querying, tracking, and management.

**Operations**:
- Filter: Search by order number, type, transaction status, and time.
- View: Detailed fields of the order's payment.
