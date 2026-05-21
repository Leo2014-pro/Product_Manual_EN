# Global Collection


### Module Definition

The global collection system receives funds from different countries and networks and consolidates them into the ledger system.

### Design Goals

- Connect global fund entry points
- Support unified crediting for fiat and digital assets
- Reduce cross-border collection complexity
- Provide a unified fund view

### Fiat Collection Capabilities

Supports the following collection methods:
- Local Collection Accounts
- SWIFT cross-border remittance
- Local Rails
- Multi-Currency Accounts

Supported currencies:
- USD / EUR / GBP / SGD / HKD, etc.

### Digital Asset Collection Capabilities

Supports major cryptocurrencies (including but not limited to):
- USDT
- USDC
- BTC
- ETH

Capabilities include:
- Multi-chain address management (ERC20 / TRC20, etc.)
- On-chain Listener
- Automatic crediting to the asset system
- Ledger Mapping

### Example Flow (E-commerce Collection)

- User pays USD or USDT
- Funds enter the collection account (Bank / Wallet Address)
- System automatically identifies the fund type
- Writes to the unified ledger system
- Enters the merchant asset account
- Available for subsequent payments or settlement
