from datetime import datetime,timezone
from hashlib import sha256
import json
class Blockchain:
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
        # Compute hash for genesis block
        genesis_block['hash'] = self.hash(genesis_block)
        self.chain.append(genesis_block)
        
    

    @property
    def prev_hash(self):
        if not self.chain:
            return '0'*16
        return self.chain[-1]['hash']
    @property
    def difficulty(self):
        return 3
    @staticmethod
    def hash(block):
        data=json.dumps(block,sort_keys=True).encode()
        return sha256(data).hexdigest()
    
    def valid_hash(self,hash):
        return hash.startswith('0'*self.difficulty)
    
    
    
    def new_block(self):
        block={'Id':len(self.chain),
               'Timestamp':datetime.now(timezone.utc).isoformat(),
               'Transactions':self.pending_transaction,
               'prev_hash':self.prev_hash,
               'nonce':0
               }
        return block
    



    def add_transaction(self,sender:str,recipient:str,amount:str):
        self.pending_transaction.append({'sender':sender,
                                         'recipient':recipient,
                                         'amount':amount})
        




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
            self['nonce']+=1

        
    def rem_block(self,):
        if len(self.chain)>1:
            self.chain.pop()
    
    def save_chain_to_file(self, filename='blockchain.txt'):
        with open(filename, 'w') as f:
            json.dump(self.chain, f, indent=4)
    def append_block_to_file(self, block, filename='blockchain.txt'):
        with open(filename, 'a') as f:
            f.write(json.dumps(block, sort_keys=True) + '\n')
