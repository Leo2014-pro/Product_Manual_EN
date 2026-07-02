# Virtual Account System

### Module Definition

The Virtual Account System is the "Ledger Layer" of the entire fund infrastructure.

### Design Goals

- Digitize fund structures
- Support multi-tier account hierarchy
- Enable real-time reconciliation
- Support unified multi-currency management

### Account Structure

Supports a multi-level hierarchy:
- Platform Account
- Merchant Account
- User Account

### Core Capabilities

- Multi-currency balance system
- Real-time ledger updates
- Auto reconciliation
- Internal transfers between accounts
- API-based account creation and management

### Example (Fund Flow)

- User top-up → User VA
- Merchant revenue → Merchant VA
- Platform fees → Platform VA
All movements are recorded in the unified ledger.
