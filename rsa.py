from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
#Generate private key
private_key = rsa.generate_private_key(
    public_exponent=65537,
    key_size=3072,
    backend=default_backend()
)

#Generate public key
public_key = private_key.public_key()

#Serialize private key
pem = private_key.private_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PrivateFormat.PKCS8,
    encryption_algorithm=serialization.NoEncryption()
)

#Serialize public key
pem2 = public_key.public_bytes(
    encoding=serialization.Encoding.PEM,
    format=serialization.PublicFormat.SubjectPublicKeyInfo
)

#Save private key to file
f = open("privkey.pem", "wb")
f.write(pem)
f.close()

#Save public key to file
f = open("pubkey.pem", "wb")
f.write(pem2)
f.close()
 
#Load the private and public key from file and use it to encrypt and decrypt the message.

#Load private key from file
with open("privkey.pem", "rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None,
        backend=default_backend()
    )

#Load public key from file
with open("pubkey.pem", "rb") as key_file:
    public_key = serialization.load_pem_public_key(
        key_file.read(),
        backend=default_backend()
    )

with open("sensitive.txt", "rb") as f:
    message = f.read(307)


#Encrypt the message
ciphertext = public_key.encrypt(
    message,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# write encrypted content into "sensitive.enc.txt"
f = open("sensitive.enc.txt", "wb")
f.write(ciphertext)
f.close()

print(ciphertext)
#Decrypt message
plaintext = private_key.decrypt(
    ciphertext,
    padding.OAEP(
        mgf=padding.MGF1(algorithm=hashes.SHA256()),
        algorithm=hashes.SHA256(),
        label=None
    )
)

# write decrypted content into "sensitive.txt"
 # write encrypted content into "sensitive.enc.txt"
f = open("sensitive.dec.txt", "wb")
f.write(plaintext)
f.close()   
print(plaintext)