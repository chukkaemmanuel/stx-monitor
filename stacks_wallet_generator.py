#!/usr/bin/env python3

from stacks_blockchain import Stacks

# Replace 'YOUR_MNEMONIC' with your actual mnemonic
mnemonic = "your_mnemonic_phrase"

# Connect to Stacks Testnet
stacks = Stacks(network="testnet")

# Derive Stacks address
address = stacks.derive_address_from_seed(mnemonic)

# You can then use the address for balance checks or other operations
print(f"Stacks Address: {address}")