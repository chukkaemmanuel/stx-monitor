#!/usr/bin/python3

import requests


def get_stacks_balance(addr):
    url = f"https://api.testnet.hiro.so/extended/v1/address/{addr}/balances"
    r = requests.get(url)
    if r.status_code != 200:
        return None
    
    data = r.json()
    stx_balance = int(data['stx']['balance']) / 10**6
    return stx_balance

def main():
    mnemonic = "twice kind fence tip hidden tilt action fragile skin nothing glory cousin green tomorrow spring wrist shed math olympic multiply hip blue scout claw"
    num_addrs = 100

    try:
        addrs = gen_stacks_addr(mnemonic, num_addrs)


        for i , addr in enumerate(addrs):
            balance = get_stacks_balance(addr)
            if balance is not None and balance > 0:
                print(f"Address {i + 1}: {addr}")
                print(f"Balance: {balance} STX")
                print("---")
            else:
                print(f"Address {i + 1}: {addr}")
                print("Failed to get balance")
                print("---")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
        print("Please make sure you have the latest version of bip_utils installed.")
        print("You can update it using: pip install --upgrade bip_utils")


if __name__ == "__main__":
    main()