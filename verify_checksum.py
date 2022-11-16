import hashlib

def verify_checksum(filename, checksum_file):
    sha256 = hashlib.sha256()

    with open(filename, 'rb') as f:
        while True:
            data = f.read(65536)
            if not data:
                break
            sha256.update(data)

    with open(checksum_file, 'r') as f:
        checksum = f.read()

    if sha256.hexdigest() == checksum:
        print('Accept!')
    else:
        print('Reject!')


verify_checksum('sensitive.txt', 'sensitive_checksum.txt')
