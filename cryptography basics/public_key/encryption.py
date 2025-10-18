from nacl.public import PrivateKey,Box
alice_private=PrivateKey.generate()
bob_private=PrivateKey.generate()

alice_public=alice_private.public_key
bob_public=bob_private.public_key

bobs_box=Box(bob_private,alice_public)
encrypted=bobs_box.encrypt(b'I\'m the killer')
print(encrypted)

alice_box=Box(alice_private,bob_public)
data=alice_box.decrypt(encrypted)
print(data.decode())