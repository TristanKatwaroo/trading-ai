# Trading AI

A cryptocurrency trading software currently in development. Planning on expanding to FOREX and stock exchanges in the future.

## Getting Started

Launch contents of balanceViewer in a Python IDE.

### Prerequisites

A binance account is needed to use this software.

<b>Click [here](https://www.binance.com/?ref=16527883) to create an account if you don't already have one.</b>
    
 After logging into Binance, follow the following steps to create your API keys:
    
    1. Navigate to your account settings
    2. Select API Setting and enter a name for your API key label
    3. Save your secret key and your api key in a safe location
    4. Your secret key will only be viewable once, so ensure you have a copy of this
    5. Ensure the following options are enabled:
      [x] Read info
      [x] Enable trading
      [x] Enable withdrawals
    6. Select the option "Restrict access to trusted IPs only" and enter your IP address
    7. Save changes

### Setup

After initializing API keys, enter them into lines 7 and 8 of balanceViewer.py

```
api_secret = 'enter secret key here'
api_key = 'enter key here'
```

## Running the software

Run balanceViewer.py

Enter a command (currently balance and stop are the only available commands).

```
stop = ends program
balance = checks balance of a particular asset
```

Enter a coin to view your balance (eg. "btc").

