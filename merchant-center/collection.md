# Collection

Collection is the core functional module for merchants to manage all **inbound collection** (receiving funds from users) orders and track fund status.

## Payment Links

### Link List

- **Feature Description**: This module displays all created collection links.

- **Operations**:
  - Filter: Search by identifier, product name, time, and other criteria.
  - View: View detailed information of a payment link, as well as orders associated with that payment link.
  - Delete: After deleting a link, that payment link becomes invalid.
  - Copy: Click the "Copy Link" button to share the URL with buyers for payment.
  - Add: Generate a fixed collection link for buyers, with flexible parameter configuration:
    1. **Link Basic Information**:
       - Product Name, Product Description: Displayed on the payment checkout page.
       - Image: If not set, the merchant logo is displayed.
       - Advanced Settings: If configured, users will need to fill in the corresponding information on the payment checkout page.
       - Pricing Currency: The currency used for calculating the price of this payment link.
       - Pricing Amount: The amount the user needs to pay; if left blank, the user fills it in on the checkout page.
    2. **Link Configuration**:
       - Type: Choose between crypto or fiat (single selection); determines the payment methods available to the user at the time of payment.
       - Currency/Amount: Based on the selected type, choose the specific currency and order amount.
       - Link Type: Single-use / Multi-use; determines whether this link can initiate a transaction once or repeatedly.
       - Link Validity Period: Currently supports 4 options: 24h / 48h / Long-term / Custom (within a six-month window).

---

## Crypto Collection Orders

**Feature Description**: This page centrally displays your digital currency collection order records for easy querying, tracking, and management. Includes data from both API-placed orders and payment link orders.

**Operations**:
- Filter: Search by order number, type, transaction status, and time.
- View: Detailed fields of the order's top-up.
  - Order Status: Only after the order is successful will it be credited to the merchant's frozen assets.
  - Settlement Status: Only when settlement becomes successful will it be credited to the merchant's available assets.
  - Callback Notification: After a successful callback, it indicates that the downstream interface has been notified.
- Switch Status: This operation only exists in the sandbox environment and is used for debugging during API integration.

---

## Fiat Collection Orders

**Feature Description**: This page centrally displays your fiat currency collection order records for easy querying, tracking, and management. Includes data from both API-placed orders and payment link orders.

**Operations**:
- Filter: Search by order number, type, transaction status, and time.
- View: Detailed fields of the order's top-up.
  - Order Status: Only after the order is successful will it be credited to the merchant's frozen assets.
  - Settlement Status: Only when settlement becomes successful will it be credited to the merchant's available assets.
  - Callback Notification: After a successful callback, it indicates that the downstream interface has been notified.
- Switch Status: This operation only exists in the sandbox environment and is used for debugging during API integration.
