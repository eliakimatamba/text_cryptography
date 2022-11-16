import hashlib

def compute_checksum(filename):
    sha256 = hashlib.sha256()

    with open(filename, 'rb') as f:
        while True:
            data = f.read( 65536)
            if not data:
                break
            sha256.update(data)

    checksum = sha256.hexdigest()

    with open('sensitive_checksum.txt', 'w') as f:
        f.write(checksum)

compute_checksum('sensitive.txt')
