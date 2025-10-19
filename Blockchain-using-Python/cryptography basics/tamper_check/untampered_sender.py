from hashlib import sha256
message='This is to check if the integrity of a message sent via public network'
data=sha256((message.strip() + 'p@ssword').encode()).hexdigest()
with open('message','w') as f:
    f.write(message)
    f.write(f'\n{data}')