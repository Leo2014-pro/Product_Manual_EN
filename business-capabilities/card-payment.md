# Card Payment

### Module Definition

The Card Payment System handles global Visa / Mastercard payment requests.

### Design Goals

- Improve payment success rates
- Support global card networks
- Multi-channel fault tolerance
- Support subscriptions and recurring payments

### Payment Capabilities

Supported features:
- One-time Payment
- Recurring Payment (Subscription)
- 3DS verification flow
- Multi-currency payment and settlement

### Routing Mechanism

The system has a built-in routing engine:
- Channel selection based on country / card type
- Real-time success rate calculation
- Automatic fallback (failure switching)
- Cost optimization strategy

### Example (Payment Flow)

- User initiates payment
- System selects the optimal PSP channel
- Initiates Visa / Mastercard request
- Returns authorization result
- Records are written to the VA ledger system
- Transaction status is updated
