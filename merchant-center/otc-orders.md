# OTC Orders

When using OSL upstream for OTC (Over-The-Counter) services, this module is available. All merchant KYB and related information is onboarded through OSL, and every deposit/withdrawal order is processed through OSL. The platform only transparently transmits data to the upstream.

## Accounts

**Feature Description**: This page is used for opening OTC accounts, displaying OTC account VA collection information, and digital asset status.

**Operations**:
1. Open OTC Account
   1. Complete KYB by filling in the required information.
   2. Fill in fiat account card-opening information to proceed with account opening.
2. View
   1. View fiat receiving bank account details.
   2. View USDT and USDC asset status.

---

## Collections

**Feature Description**: Merchants can view the receiving account information for their OTC accounts.

**Operations**:
1. Deposit Preparation
   1. Before receiving funds, you must add counterparties and their receiving wallet addresses / bank account numbers.
   2. When an account is created, a self-owned counterparty is created by default.
2. Deposit Details
   1. **Crypto**: Displays the receiving wallet address for that counterparty. When funds are received at this wallet address, it is recorded as a transfer from that counterparty by default.
   2. **Fiat**: Displays receiving bank information and the paying company name. You must use an account with the same name as the counterparty to transfer funds; otherwise, the funds cannot be credited.

---

## Payouts

**Feature Description**: Merchants can perform payout operations from their OTC accounts.

**Operations**:
1. Payee Information
   1. Before making a payment, you must add counterparties and their receiving wallet addresses / bank account numbers.
   2. When selecting a third-party counterparty, you must first add a payout limit in the Counterparty module before making a payment. No limit is required for payments to yourself.

2. Payout Details
   1. **Crypto**:
      - Enter the payout amount and purpose.
      - Payout fees are deducted from the account balance.
      - Review the receiving wallet address and counterparty to verify correctness.
      - After submitting the order, check the order status in the Payout Order list.

   2. **Fiat**:
      - Enter the payout amount and purpose.
      - Review the receiving bank information and counterparty to verify correctness.
      - After submitting the order, check the order status in the Payout Order list.

---

## Counterparties

**Feature Description**: Maintain counterparty company information, deposit/withdrawal accounts, and payout limits for merchant fund inflows and outflows.

**Operations**:

1. **Counterparties**: Serves as the counterparty entity for fund inflows and outflows, with deposits and withdrawals tracked by counterparty.
   1. Create Counterparty: Create a company entity that transacts with the merchant.
   2. Edit: Edit the alias.
   3. Entity Type:
      - Self: The entity created from the merchant's own KYB information, automatically created when the OTC account is opened. No limit is required for payouts from this entity.
      - Third-Party: Other company entities.

2. **Counterparty - Upload Documents**
   1. Upload invoices and contracts. Once approved, a payout limit to that company is granted.
   2. Uploaded document limits are cumulative.

3. **Counterparty - Limit Management**
   1. All currency payout limits are unified in USD. When a merchant makes a payout, the limit is deducted accordingly.

4. **Counterparty - Crypto**
   1. Deposit
      - List: Displays multiple deposit addresses for this counterparty. Any amount transferred to wallet addresses in the list is recorded as a transfer from that counterparty.
      - Add: Create a new wallet address for the merchant to receive funds.
   2. Withdrawal
      - List: Displays multiple withdrawal addresses for this counterparty. When the merchant pays this counterparty in crypto, the address must be one of the approved addresses in this list.
      - Add: Create a new withdrawal wallet address.
      - Disable/Enable: Once disabled, the address cannot be selected for payouts.

5. **Counterparty - Fiat**
   1. Deposit
      - List: Displays multiple paying bank accounts for this merchant. When this counterparty pays the merchant, the transfer must come from a bank account added in this list.
      - Add: Create a new deposit channel, which must be a bank account under the same name as the counterparty.
   2. Withdrawal
      - List: Displays multiple receiving bank accounts for this counterparty. When the merchant pays this counterparty in fiat, the account must be one of the approved bank accounts in this list.
      - Add: Create a new withdrawal bank account.
      - Disable/Enable: Once disabled, the account cannot be selected for payouts.

---

## Collection Orders

**Feature Description**: Management and viewing of merchant OTC account top-up orders.

**Operations**:
1. Add Counterparty: When a user who has not added a counterparty transfers funds to the merchant's bank account, they must first go to Counterparties and add a counterparty with the same name for the order to proceed.
2. Manual Credit: When receiving fiat funds, you must select a digital currency for conversion. Once confirmed, the order proceeds and is ultimately settled in the selected digital currency into the OTC account.

---

## Payout Orders

**Feature Description**: View merchant OTC account withdrawal orders.
