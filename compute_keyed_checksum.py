import hmac

def compute_keyed_checksum(filename, key_file):
    with open(key_file, 'rb') as f:
        key = f.read()

    hmac_sha256 = hmac.new(key, None, 'sha256')

    with open(filename, 'rb') as f:
        while True:
            data = f.read(65536)
            if not data:
                break
            hmac_sha256.update(data)

    checksum = hmac_sha256.hexdigest()

    with open('sensitive_keyed_checksum.txt', 'w') as f:
        f.write(checksum)

compute_keyed_checksum('sensitive.txt', 'key.bin')
