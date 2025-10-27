import hashlib, json

class Transaction:
    def __init__(self, sender:str, receiver:str, amount:float, nonce:int, base_fee:float, fee_limit:float):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.nonce = nonce
        self.base_fee = base_fee
        self.fee_limit = fee_limit
        self.txID = self.string_to_hex(self.__dict__)

    def string_to_hex(self, data):
        b = json.dumps(data, sort_keys=True).encode()
        hashed = hashlib.sha3_256(b)
        return hashed.hexdigest()



if __name__=="__main__":
    tx=Transaction('giver','taker',100,0,.1,1)
    print(tx.txID)