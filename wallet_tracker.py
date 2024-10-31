#!/usr/bin/python3

import sys
import requests


def get_stacks_balance(addr):
    url = f"https://api.testnet.hiro.so/extended/v1/address/{addr}/balances"
    r = requests.get(url)
    if r.status_code != 200:
        return None
    
    data = r.json()
    stx_balance = int(data['stx']['balance']) / 10**6
    return stx_balance

def monitor_wallets(wallet_list):
    for i, wallet in enumerate(wallet_list):
        balance = get_stacks_balance(wallet)
        if balance is not None and balance > 0:
            print(f"Address: {i + 1}: {wallet}")
            print(f"Balance: {balance} STX")
            print("---")
        else:
            print(f"Address {i + 1}: {wallet}")
            print("Failed to get balance")
            print("---")

def main():
    if len(sys.argv) < 2:
        print("Please provide at least one wallet address as a command-line argument.")
        sys.exit(1)

    wallet_list = sys.argv[1:]

    try:
        monitor_wallets(wallet_list)
    except Exception as e:
        print(f"An error occurred: {str(e)}")

if __name__ == "__main__":
    main()