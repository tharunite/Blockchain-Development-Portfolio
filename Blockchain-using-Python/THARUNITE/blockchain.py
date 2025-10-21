from datetime import datetime,timezone
from hashlib import sha256
import json
from ecdsa import SigningKey,VerifyingKey,SECP256k1

class Blockchain:
    #initiating with empty chain and empty transactions list
    def __init__(self):
        self.chain=[]
        self.pending_transaction=[]
        # Create genesis block
        genesis_block = {
            'Id': 0,
            'Timestamp': datetime.now(timezone.utc).isoformat(),
            'Transactions': [],
            'prev_hash': '0'*16,
            'nonce': 0
        }
        genesis_block['hash'] = self.hash(genesis_block)
        self.chain.append(genesis_block)
        
    



#UTILITY functions
    @property
    #get the previous hash of the chain for the block
    def prev_hash(self):
        if not self.chain:
            return '0'*16
        return self.chain[-1]['hash']
    @property
    #can be changed later , but for now hard coded
    def difficulty(self):
        return 3
    @staticmethod
    def hash(block):
        data=json.dumps(block,sort_keys=True).encode()
        return sha256(data).hexdigest()
    
    def valid_hash(self,hash):
        return hash.startswith('0'*self.difficulty)
    
    
    
    
    







    #Flow:add transaction -> verify transaction -> sign transaction -> add to pending transaction 
    #once 3 transactions are reached new block is created pow -> add block - > add to chain 

    def new_transaction(self, sender:str, recipient:str, amount:int):
        tx = {
            "sender's public_key": sender,
            "recipient's public_key": recipient,
            "amount": amount
        }
        # Validate & sign
        self.validate_transaction(tx)  # adds 'signature'
        # Append to pending
        self.pending_transaction.append(tx)
        return tx
    

    def validate_transaction(self,transaction):
        with open('accounts', 'r') as f:
            data = json.load(f)

        sender = None
        receiver = None

        for user in data:
            if user['public_key'] == transaction["sender\'s public_key"]:
                sender = user
            if user['public_key'] == transaction["recipient\'s public_key"]:
                receiver = user
        if not sender or not receiver:
            raise ValueError('Invalid Transaction')
        if sender['balance'] < transaction['amount']:
            raise ValueError('Insufficient balance')
        signature=self.sign_transaction(sender['private_key'],transaction)
        transaction['signature']=signature.hex()

    

    def sign_transaction(self,privatekey,transaction):
        data=transaction.copy()
        data.pop('signature', None)
        message_hash = sha256(json.dumps(data, sort_keys=True).encode()).digest()
        signature_value=SigningKey.from_string(bytes.fromhex(privatekey),curve=SECP256k1)
        signature=signature_value.sign(message_hash)
        return signature
    def verify_transaction(self,transaction):
        tx_copy = transaction.copy()
        sig = tx_copy.pop('signature')
        h = sha256(json.dumps(tx_copy, sort_keys=True).encode()).digest()
        vk = VerifyingKey.from_string(bytes.fromhex(tx_copy["sender's public_key"]), curve=SECP256k1)
        return vk.verify(bytes.fromhex(sig), h)
   
   
   
   
   
   
   
   
   
   
   
   
   
   
    def new_block(self):
        block = {
            'Id': len(self.chain),  # automatically continues
            'Timestamp': datetime.now(timezone.utc).isoformat(),
            'Transactions': self.pending_transaction,
            'prev_hash': self.prev_hash,
            'nonce': 0
        }
        return block

    

    def pow(self):
        block=self.new_block()
        while True:
            hashed_block=self.hash(block)
            if self.valid_hash(hashed_block):

                block['hash']=hashed_block
                self.chain.append(block)
                self.pending_transaction=[]
                self.append_block_to_file(block)
                break
            block['nonce']+=1

        
    
    
    
    
    
    
    
    
    #saving
    def save_chain_to_file(self, filename='blockchain.txt'):
        with open(filename, 'w') as f:
            json.dump(self.chain, f, indent=4)
    def append_block_to_file(self, block, filename='blockchain.txt'):
        with open(filename, 'a') as f:
            f.write(json.dumps(block, sort_keys=True) + '\n')
    def load_chain_from_file(self, filename='blockchain.txt'):
        self.chain = []
        try:
            with open(filename, 'r') as f:
                for line in f:
                    block = json.loads(line)
                    self.chain.append(block)
        except FileNotFoundError:
            # If no file exists, create genesis block
            genesis_block = {
                'Id': 0,
                'Timestamp': datetime.now(timezone.utc).isoformat(),
                'Transactions': [],
                'prev_hash': '0'*16,
                'nonce': 0
            }
            genesis_block['hash'] = self.hash(genesis_block)
            self.chain.append(genesis_block)


