# Virtual Accounts


### Module Definition

The virtual account system serves as the "Ledger Layer" of the entire fund infrastructure.

### Design Goals

- Digitize fund structures
- Support multi-tier account hierarchy
- Enable real-time reconciliation
- Support unified multi-currency management

### Account Structure

Supports multi-level hierarchy:
- Platform Account
- Merchant Account
- User Account

### Core Capabilities

- Multi-currency balance system
- Real-time Ledger updates
- Auto Reconciliation
- Internal Transfer between accounts
- API-based account creation and management

### Example (Fund Flow)

- User deposit → User VA
- Merchant revenue → Merchant VA
- Platform fees → Platform VA

All movements are recorded in the unified ledger.
