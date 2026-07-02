# UCard Management

The platform supports issuing virtual and physical cards, and is also compatible with shared cards where multiple sub-cards share a common project asset pool.

## UCard Account

> **UCard Fund Flow Overview**
> Merchant Crypto Account → Transfer to UCard Account → UCard Account splits into two paths:
> - Path 1: Direct top-up to a single UCard (card issuance fees, service fees, single card balance deduction)
> - Path 2: Top-up to a shared project → All sub-cards under the shared project share the same fund pool
> Funds can only come from the crypto account; the UCard account does not accept external deposits.

**Feature Description**: The UCard Account is the funding vehicle for merchants within the UCard system; all funds come from the crypto account. Card issuance, service fees, and top-ups under the UCard system are all deducted from this account.

**Operations**:

- **Transfer**: Supports fund transfers between crypto account assets and the UCard account.
- **Account Details**: View UCard account fund transaction history.

---

## Shared Projects

**Feature Description**: A mechanism where multiple sub-cards share the same project fund pool, supporting project creation, sub-card addition, and project top-ups/withdrawals.

**Operations:**

- **Create Project**: Shared Project → Add Project → Fill in name/top-up amount/select card BIN, etc. → Confirm creation.
- **Top-Up**: Shared Project → Details → Top-Up → Enter amount → Confirm.
- **Transfer Out**: Shared Project → Details → Withdraw → Enter amount → Confirm.
- **Add Sub-Card**: Shared Project → Add Shared Card → Select UCard → Select cardholder and configure spending limit → Confirm.
- **Freeze/Unfreeze Sub-Card**: Shared Project → Details → Select sub-card → Freeze/Unfreeze. Frozen sub-cards are unavailable.
- **Freeze Project**: Shared Project → Details → More → Freeze. All sub-cards become unavailable once frozen.
- **View**:
  - Details - Sub-Card List: View all sub-card information and manage sub-cards.
  - Transaction History: Displays the fund transaction history of the shared project.

---

## Card Management

> **Card Type Comparison**
>
> | Dimension | Virtual Card | Physical Card | Shared Card |
> |-----------|-------------|---------------|-------------|
> | Issuance Entry | Card Management | Card Management | Shared Project (not issued via Card Management) |
> | Funding Source | UCard Account | UCard Account | Shared Project Fund Pool |
> | Use Case | Online payments, instant issuance | Offline swiping, physical delivery | Team/Project shared funds |
> | Status Management | Freeze/Unfreeze/Cancel | Freeze/Unfreeze/Cancel | Managed under Shared Project |

**Feature Description**: Manage the full lifecycle of all UCards (virtual/physical), including card issuance, status management, and queries. The list also displays shared cards (shared card issuance and top-up entry points are in the "Shared Projects" module; this module only supports viewing and status management).

**Operations:**

- **Add (Issue Card)**:
  - Physical Card: Card Management → Issue Card → Select card type (Virtual/Physical) → Select card BIN/card scheme → Select cardholder → Enter card number → Set PIN → Confirm issuance (card issuance fee automatically deducted).
  - Virtual Card: Card Management → Issue Card → Select card type (Virtual/Physical) → Select card BIN/card scheme → Select cardholder → Top-up amount → Confirm issuance (card issuance fee automatically deducted).
  - Note: Shared cards are issued through the Shared Project module.

- **Details**: Card Management → List → Click a card → View complete information (card number/cardholder/balance/limits/status/transaction records).
- **Status Change**: Card Management → List → Action column → Freeze/Unfreeze/Copy/Cancel.
- **Top-Up**:
  - Regular Card: Top-up deducts funds from the UCard account.
  - Shared Card: Modify total credit limit without adjusting funds.
- **Transfer Out**:
  - Regular Card: Transfer out to UCard account.
  - Shared Card: Modify total credit limit without adjusting funds.
- **Filter**: Card Management → List → Filter by status/card type/cardholder/card number/project.

---

## 3DS Verification

**Feature Description**: Records 3DS secondary verification information triggered during UCard online payments, supporting verification record queries.

**Operations**: Filter: 3DS Verification → Verification Records → Set time/card number/cardholder/verification result/amount range → Query/Export.

---

## Transaction Inquiry

**Feature Description**: The entry point for querying all UCard spending records, supporting multi-dimensional filtering, detail viewing, and export for reconciliation.

**Operations**:
- Filter: Transaction Inquiry → List → Set time/card number/cardholder/card type/project/status/type/amount/merchant/keyword → Query/Export.

---

## Cardholder Management

**Feature Description**: Manage UCard cardholder information. This is a prerequisite module for card issuance — cardholders must be created first.

**Operations**:

- **Add**: Cardholder Management → Add Cardholder → Fill in basic information (name/ID/phone/address) → Upload ID → Submit.
- **Details**: View complete information and associated cards.
- **Freeze/Enable**: Deactivate/Activate.
- **Delete (Deregister)**: Cardholder Management → List → Action column → Deregister (all cards under the cardholder must be handled first).
- **Filter**: Cardholder Management → List → Filter by KYC status/nationality/cardholder status/name/phone number/ID number.
