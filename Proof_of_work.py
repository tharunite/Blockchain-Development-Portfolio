from hashlib import sha256
text=input("Enter the message: ")
target=2**250
nonce=0
while True:
    hash=sha256(text.encode()+str(nonce).encode()).hexdigest()
    output=int(hash,16)
    if(output<target):
        print("nonce: ",nonce)
        print('hash: ',hash)
        break
    print(output)
    nonce+=1