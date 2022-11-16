from cryptography.fernet import Fernet

#generate key
key = Fernet.generate_key()

#open file
f = Fernet(key)
prk = open("pub_key.key","wb")
prk.write(key)
prk.close()

with open('sensitive.txt', 'rb') as orgfile:
    org = orgfile.read()

#encrypt the text file
encrypted = f.encrypt(org)

with open ('sensitive.enc.txt', 'wb') as encrypted_file:
    encrypted_file.write(encrypted)

#read the key and store it in a variable
with open('pub_key.key', 'rb') as vkey:
    key_var = vkey.read()

#open file
f = Fernet(key_var)

with open('sensitive.enc.txt', 'rb') as encrypted_file:
    encrypted = encrypted_file.read()

print(encrypted)

#decrypt the text
decrypted = f.decrypt(encrypted)

print(decrypted)

#write decrypted file
with open('sensitive.dec.txt', 'wb') as decrypted_file:
    decrypted_file.write(decrypted)