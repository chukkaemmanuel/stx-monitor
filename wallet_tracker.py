#!/usr/bin/python3

import sys
import requests
import time


def get_stacks_balance(addr):
    chain = sys.argv[1]
    if chain not in ["mainnet", "testnet"]:
        raise ValueError("Invalid chain name. Please use 'mainnet' or 'testnet'.")

    url = f"https://api.{chain}.hiro.so/extended/v1/address/{addr}/balances"
    r = requests.get(url)
    if r.status_code != 200:
        return None
    
    data = r.json()
    stx_balance = int(data['stx']['balance']) / 10**6
    return stx_balance

def monitor_wallets(wallet_list):
    initial_balances = {addr: get_stacks_balance(addr) for addr in wallet_list}

    print("Initial Wallet Balances:")
    for addr, balance in initial_balances.items():
        print(f"Address: {addr}: {balance} STX")

    while True:
        for wallet in wallet_list:
            current_balance = get_stacks_balance(wallet)
            if current_balance is not None and current_balance != initial_balances[wallet]:
                print(f"Address: {wallet} - Updated Balance: {current_balance} STX")
                initial_balances[wallet] = current_balance
        time.sleep(10)

def main():
    if len(sys.argv) < 3:
        print("Please provide at least one wallet address as a command-line argument.")
        sys.exit(1)

    wallet_list = sys.argv[2:]

    try:
        monitor_wallets(wallet_list)
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()