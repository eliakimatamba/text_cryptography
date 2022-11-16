from cryptography.hazmat.primitives import padding
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import rsa
from cryptography.hazmat.primitives.asymmetric import padding

#Load the private and public key from file and use it to encrypt and decrypt the message.

#Load private key from file
with open("priv_key", "rb") as key_file:
    private_key = serialization.load_pem_private_key(
        key_file.read(),
        password=None,
        backend=default_backend()
    )

#Load public key from file
with open("pub_key", "rb") as key_file:
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
f = open("sensitive.txt", "wb")
f.write(ciphertext)
f.close()

