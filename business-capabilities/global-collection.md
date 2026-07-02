# Global Collection

### Module Definition

The Global Collection System is designed to receive funds from different countries and networks and consolidate them into the ledger system.

### Design Goals

- Connect global fund entry points
- Support unified fiat + digital asset crediting
- Reduce cross-border collection complexity
- Provide a unified fund view

### Fiat Collection Capabilities

Supported collection methods:
- Local bank account collection (Local Collection Accounts)
- SWIFT cross-border remittance
- Local clearing networks (Local Rails)
- Multi-currency account system (Multi-Currency Accounts)

Supported currencies:
- USD / EUR / GBP / SGD / HKD, etc.

### Digital Asset Collection Capabilities

Supported major cryptocurrencies (including but not limited to):
- USDT
- USDC
- BTC
- ETH

Capabilities include:
- Multi-chain address management (ERC20 / TRC20, etc.)
- On-chain transaction listener
- Automatic crediting to the asset system
- Transaction and ledger mapping

### Example Flow (E-commerce Collection)

- User pays in USD or USDT
- Funds enter the collection account (Bank / Wallet Address)
- System automatically identifies the fund type
- Records are written to the unified ledger system
- Funds enter the merchant asset account
- Available for subsequent payments or settlements
