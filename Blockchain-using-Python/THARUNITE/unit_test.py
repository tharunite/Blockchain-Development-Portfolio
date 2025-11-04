import json
import random
from ecdsa import SigningKey, SECP256k1
from blockchain import Blockchain 
from datetime import datetime,timezone


def generate_accounts(num):
    accounts = []
    for _ in range(num):
        sk = SigningKey.generate(curve=SECP256k1)
        vk = sk.verifying_key
        accounts.append({
            "private_key": sk.to_string().hex(),
            "public_key": vk.to_string().hex(),
            "balance": 100
        })
    return accounts

accounts = generate_accounts(6)  


with open("accounts", "w") as f:
    json.dump(accounts, f, indent=4)


bc = Blockchain()
bc.load_chain_from_file()  


tx_per_block = 3
total_blocks = 5
block_counter = 0

while block_counter < total_blocks:
    print(f"\n--- Preparing Block {block_counter+1} ---")
    for _ in range(tx_per_block):
        sender, receiver = random.sample(range(len(accounts)), 2)
        amount = random.randint(1, 20)
        try:
            tx = bc.new_transaction(
                accounts[sender]['public_key'],
                accounts[receiver]['public_key'],
                amount
            )
            print(f"Tx: {sender} -> {receiver} | Amount: {amount}")
        except Exception as e:
            print(f"Transaction failed: {e}")


    for tx in bc.pending_transaction:
        if bc.verify_transaction(tx):
            continue
        else:
            print("Invalid transaction found!")

    print("Mining block...")
    bc.pow()
    print(f"Block {block_counter+1} mined.")
    block_counter += 1


print("\nFinal Blockchain:")
for i, block in enumerate(bc.chain):
    print(f"\nBlock {i}:")
    print(json.dumps(block, indent=4))





