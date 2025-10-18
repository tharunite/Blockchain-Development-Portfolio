from nacl import signing,encoding
bob_private_key=signing.SigningKey.generate()
bob_public_key=bob_private_key.verify_key

bobs_public_key_hex=bob_public_key.encode(encoder=encoding.HexEncoder)

signed=bob_private_key.sign(b'I stole the bank')
print(signed)
print(bob_public_key)
print(bobs_public_key_hex)

