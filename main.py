import os
import requests
from eth_account import Account
 
# Generate a random private key
def generate_private_key():
    return os.urandom(32).hex()
 
# Derive address from private key
def private_key_to_address(private_key):
    return Account.from_key(private_key).address
 
# Check balance of address using Infura API
 
private_key_ETH = '45a5d2ec7055c392ec46bbd089d22ba2c0fc14105560e0b8cb5a55181220a831'
 
def get_balance(address):
    api_key = "cec17ce1af8446de9046be035d8c96a4"# Replace this with your Infura API key
    url = f"https://mainnet.infura.io/v3/{api_key}"
    data = {"jsonrpc":"2.0","method":"eth_getBalance","params":[address,"latest"],"id":1}
    response = requests.post(url, json=data)
    balance_wei = int(response.json()["result"], 16)
    return balance_wei / 10**18  # Convert from wei to ether
 
# Main function to generate private keys, check balances, and stop when non-zero balance is found
def main():
    while True:
        private_key = generate_private_key()
        address = private_key_to_address(private_key)
        balance = get_balance(address)
        print("Private Key:", private_key)
        print("Address:", address)
        print("Balance (ETH):", balance)
        if balance > 0:
            print("Found a non-zero balance. Stopping...")
            break
 
if __name__ == "__main__":
    main()
