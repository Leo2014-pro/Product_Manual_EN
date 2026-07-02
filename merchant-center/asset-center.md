# Asset Center

The Asset Center is primarily used for managing merchant funds.

## Asset Accounts

**Feature Description**: This page provides a centralized overview of all asset balances held by the merchant on the platform, and offers entry points for fiat and digital currency deposits and withdrawals, as well as VA assets and UCard accounts.

**Operations**:

1. **View Asset Overview**:
   - Upon entering the page, the system displays the following asset balances categorized in a list format:
     - **Fiat Assets**: Displays "Available Balance", "Frozen Amount", and "Rolling Reserve" by currency (e.g., CNY, USD).
     - **Digital Assets**: Displays "Available Balance" and "Frozen Amount" by currency (e.g., USDT, BTC).
     - **VA Account Assets**: Used for managing the merchant's global VA collection/payout funds and account balances.
     - **UCard Account Assets**: USDT only, used for card issuance, card top-ups, and related capabilities.

2. **Deposit Operations**:
   - On the asset card of the corresponding currency, click the "Deposit" button.
   - The system will guide you to different deposit flows based on the currency type:
     - **Fiat Deposit**: Redirects to the cashier for top-up; deposit orders can be viewed under Collection Orders.
     - **VA Deposit**: You may select the merchant's own VA account for receiving funds; deposit orders can be viewed under Transfer-In Records.
     - **Digital Currency Deposit**: The system generates a dedicated **deposit address** (or QR code); the merchant transfers funds to this address.

3. **Withdrawal Operations**:
   - On the asset card of the corresponding currency, click the "Withdraw" button.
   - The system guides you to the "External Payment" page, pre-selecting the corresponding currency. The merchant must fill in the withdrawal amount, select the receiving address, verify the fund password and Google Authenticator, and submit the request.
   - **VA Withdrawal**: Must select a designated VA account for the outflow.
   - **Fiat Withdrawal**: Specifying a payer is optional; specifying one incurs higher fees.

4. **Batch Withdrawal Operations**:
   - Batch withdrawal is only available for fiat accounts.
   - Information filled in the Excel template must use already-approved fiat withdrawal address details.

5. **Details**: View the fund transaction history for a specific currency asset.

---

## Asset Transfer-In

**Feature Description**: This page is used to query and manage all digital currency deposit records for the merchant, facilitating reconciliation of incoming funds. Fiat/VA account deposits are not currently supported.

**Operations**:
- Filter: Search by order number, address, order status, time, etc.
- View: View detailed deposit information.

---

## Asset Transfer-Out

**Feature Description**: This page is used to query and manage all fiat and digital currency withdrawal records.

**Operations**:
- View: View merchant withdrawal records for fiat and digital currencies. VA accounts coming soon!
- Filter: Search by order number, address, order status, time, etc.
- Bank Slip: When a fiat transfer-out occurs and the order status is completed, you can view and download the bank slip.

---

## Beneficiary Management

**Feature Description**: This module is used by merchants to manage receiving addresses for fiat and digital asset withdrawals, as well as designated fiat payer management. Addresses submitted by merchants must be approved by the platform before they can be used.

**Digital Asset Address Operations:**
- Filter: Search by currency.
- Edit: Modify receiving address information.
- Add:
  - Beneficiary Name: Name of the receiving address
  - Currency: Currency name
  - Chain Type: The public chain to which the currency belongs
  - Currency Address: Receiving wallet address.

**Fiat Asset Address Operations:**
- Filter: Search by currency.
- View: View information of added fiat receiving addresses.
- Add: Add new fiat receiving bank information.

**VA Beneficiary Operations:**
- Filter: Search by currency, account, beneficiary status, etc.
- You must first add a beneficiary, then add a receiving bank account based on the beneficiary.

**Payer Operations:**
- Filter: Search by currency, name, country, etc.
- View: View information of added fiat receiving addresses.
- Add: Add a new designated payer.

---

## Fee Rates

**Feature Description**: This module allows merchants to view the supported collection/payout currencies and their corresponding fee rates and settlement rules. Please contact the platform to add new currencies.

**Operations**:
- Filter: Search by currency, payment type, status, etc.
- View: View detailed information for a single currency.

---

## OTC (Over-The-Counter)

A collection of features for currency exchange between merchant fiat and digital currency accounts, viewing exchange rate quotes, and managing all exchange orders.

### Trading Pairs

**Feature Description**: This page displays all currency exchange trading pairs supported by the platform, provides real-time exchange rate information, and allows merchants to perform currency exchange operations.

**Operations**:
- Filter: Search by type and currency.
- Exchange: Select transaction type: **Buy** [target currency] or **Sell** [base currency]. Enter the amount of currency you wish to spend in the "**Amount**" field; the system will automatically calculate the amount you will receive in the "**You Get**" field based on the real-time exchange rate. Confirm the displayed **exchange rate**, **estimated fee**, and **estimated arrival amount**. Enter your **fund password and Google Authenticator code**, then click the "**Confirm**" button to submit the order.

### Trading Orders

**Feature Description**: This page centrally displays all your currency exchange order records for easy querying, tracking, and management.

**Operations**:
- Filter: Search by order number, type, transaction status, and time.
