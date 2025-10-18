from hashlib import sha256
'''before=input('Type something: ')
after=hashlib.sha256(before.encode())
print(f"Hash of the given input is: ",after.hexdigest())'''

with open('new_image.png','rb') as f:
    img_data=f.read()

print(sha256(img_data).hexdigest())
print(type(img_data),len(img_data))
