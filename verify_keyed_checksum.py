import hmac

def verify_keyed_checksum(filename, key_file, checksum_file):
    with open(key_file, 'rb') as f:
        key = f.read()

    hmac_sha256 = hmac.new(key, None, 'sha256')

    with open(filename, 'rb') as f:
        while True:
            data = f.read(65536)
            if not data:
                break
            hmac_sha256.update(data)

    with open(checksum_file, 'r') as f:
        checksum = f.read()

    if hmac_sha256.hexdigest() == checksum:
        print('Accept!')
    else:
        print('Reject!')


verify_keyed_checksum('sensitive.txt', 'key.bin', 'sensitive_keyed_checksum.txt')