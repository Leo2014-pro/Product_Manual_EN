# Card Payment


### Module Definition

The card payment system processes global Visa / Mastercard payment requests.

### Design Goals

- Improve payment success rates
- Support global card networks
- Multi-channel failover
- Support subscription and recurring payments

### Payment Capabilities

Supports:
- One-time Payment
- Recurring Payment
- 3DS verification flow
- Multi-currency payment and settlement

### Routing Mechanism

The system includes a built-in routing engine:
- Selects channel based on country / card type
- Real-time success rate calculation
- Automatic fallback on failure
- Cost optimization strategies

### Example (Payment Flow)

- User initiates payment
- System selects the optimal PSP channel
- Sends Visa / Mastercard request
- Returns authorization result
- Writes to VA ledger system
- Updates transaction status
