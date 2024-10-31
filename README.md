## Wallet Balance Monitor

This Python script allows you to monitor the balances of multiple wallet addresses on the Stacks blockchain network (either mainnet or testnet). The script displays the initial balances of the provided wallet addresses and then continuously checks for any updates in the balances due to new transactions.

### Pre-requisites

* Python 3
* Requests library (install using pip install requests)

### Usage

```bash
./wallet_balance_monitor.py [chain] [wallet_address_1] [wallet_address_2] ...
```

* chain: Specify the blockchain network to monitor (mainnet or testnet).
* wallet_address_1, wallet_address_2, ...: Provide one or more wallet addresses to monitor.

### Example

To monitor the balances of two wallet addresses on the testnet:

```bash
./wallet_balance_monitor.py testnet SP1P72K4R5RSB4ZQVQ75V2J0K0XDGQGS4M2S9Z1M8 SP3F3JG2A4GN2V9N8TBB4D8SC4K4X2VWQCT5YKV2R
```

### Functionality

1. Initializes by displaying the initial balances of the provided wallet addresses.
2. Continuously checks for balance updates at an interval of 10 seconds.
3. Prints out updated balances when a new transaction occurs on any of the monitored wallet addresses.


### Error Handling

* The script validates the provided chain name (mainnet or testnet).
* Handles errors gracefully and displays informative messages.

