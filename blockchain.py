from datetime import datetime,timezone
import json
from hashlib import sha256
import random
class Blockchain:
    def __init__(self,difficulty=4):
        self.chain=[]
        self.pending_transactions=[]
        self.difficulty=difficulty

        print("The Genesis Block is created")
        genesis_block=self.new_block(nonce=0)
        genesis_block['hash']=self.hash(genesis_block)
        self.chain.append(genesis_block)


    @property
    def prevhash(self):
        return self.chain[-1]['hash'] if self.chain else '0'*64
    
    @property
    def nonce(self):
        return random.getrandbits(64)
    
    def new_block(self,nonce):
        block={'index':len(self.chain),
               'datetime':datetime.now(timezone.utc).isoformat(),
               'transactions':self.pending_transactions.copy(),
               'previous_hash':self.prevhash,
                'nonce':nonce}
        return block
    
    def pow(self):
        nonce=self.nonce
        while True:
            block=self.new_block(nonce)
            block_hash=self.hash(block)
            if block_hash.startswith('0'*self.difficulty):
                block['hash']=block_hash
                self.chain.append(block)
                self.pending_transactions=[]
                return block
            nonce=self.nonce
            


    @staticmethod
    def hash(block):
        block_copy=block.copy()
        block_copy.pop('hash', None)
        data=json.dumps(block_copy,sort_keys=True).encode()
        return sha256(data).hexdigest()


    def new_transaction(self,sender,recipient,amount):
        self.pending_transactions.append({'sender':sender,
                                          'recipient':recipient,
                                          'amount':amount})

    def view_chain(self):
        print("\n------- Blockchain -------")
        for block in self.chain:
            print(f"Index: {block['index']}")
            print(f"Timestamp: {block['datetime']}")
            print(f"Previous Hash: {block['previous_hash']}")
            print(f"Nonce: {block['nonce']}")
            print(f"Hash: {block['hash']}")
            print("Transactions:")
            if block['transactions']:
                for t in block['transactions']:
                    print(f"  {t['sender']} -> {t['recipient']}: {t['amount']}")
            else:
                print("  No transactions")
            print("-------------------------*8")

if __name__ == "__main__":
    blockchain = Blockchain(difficulty=4)

    while True:
        print("\nOptions:")
        print("1. Add a transaction")
        print("2. Mine a block")
        print("3. View blockchain")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            sender = input("Sender: ")
            recipient = input("Recipient: ")
            amount = input("Amount: ")
            try:
                amount = float(amount)
                blockchain.new_transaction(sender, recipient, amount)
                print("Transaction added.")
            except ValueError:
                print("Invalid amount.")
        elif choice == "2":
            if not blockchain.pending_transactions:
                print("No transactions to mine!")
            else:
                blockchain.pow()
        elif choice == "3":
            blockchain.view_chain()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice, try again.")