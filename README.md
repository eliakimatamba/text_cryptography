# text_cryptography
Write a program “generate_keys”.
This program will randomly generate a pair of 3072-bit RSA keys and then it will save the public key in
to a file “pub_key” and the private key into a file “priv_key”.

 Write a program “encrypt_file”. This program will encrypt a file “sensitive.txt” on the key “pub_key”. 
 The key will be read from the file “pub_key”. 
 The encrypted file will overwrite the original file “sensitive.txt”.
 
 Write a program “compute_checksum” which computes a keyless cryptographic checksum of a file “sensitive.txt”. 
 You will use a hash function SHA256 compute it.
The checksum will be written into a file “sensitive_checksum.txt”—this file should be in the text format.

Write a program “verify_checksum” which works as follows: it computes a checksum of “sensitive.txt” and 
compares it with the contents of “sensitive_checksum.txt”.
If the resulting hash values are the same, then the program outputs “Accept!” and otherwise it outputs “Reject!”.

Write a program “compute_keyed_checksum” which works similarly to the one in Step 4, but instead of SHA256, you will use the keyed hash function HMAC-SHA256. A 256-bit key will be read from the file “key.bin”. The checksum will be written into a file “sensitive_keyed_checksum.txt”—this file should be in the text format.
Generate a random key:
head -c 256 /dev/urandom > key.bin
Copy the original (unencrypted) file “sensitive.txt” into the directory

Write a program “verify_keyed_checksum” which works as follows:
it computes a keyed checksum of “sensitive.txt” using HMAC-SHA256 and compares it with the contents of “sensitive_keyed_checksum.txt”. If the resulting values are the same, then
the program outputs “Accept!” and otherwise it outputs “Reject!”.
