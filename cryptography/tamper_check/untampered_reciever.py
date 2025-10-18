from hashlib import sha256
with open('message','r') as f:
    data=f.readlines()
message=data[0]
given=data[1]
print(message,given)
if sha256((message.strip()+'p@ssword').encode()).hexdigest() == given.strip():
    print('The message is not tampered')
else:
    print('the integrity of the message has been compromised')
