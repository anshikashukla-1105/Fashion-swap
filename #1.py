#1
from Crypto.Cipher import PKCS1_OAEP
from Crypto.PublicKey import RSA
#Generate RSA key pair
key=RSA.generate(2048)
private_key=key
public_key=key.publickey()
#create cipher objects
encrpytor=PKCS1_OAEP.new(public_key)
decrpytor=PKCS1_OAEP.new(private_key)

#message to encrypt
message=b"hello RSA!"
#encrypt
encrpyted=encrpytor.encrypt(message)
print("Encrypted:",encrpyted)
#decrypt
decrpyted=decrpytor.decrypt(encrpyted)
print("Decrypted:",decrpyted.decode())