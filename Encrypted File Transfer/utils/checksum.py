import hashlib

def sha256_checksum(data):
    return hashlib.sha256(data).hexdigest()
