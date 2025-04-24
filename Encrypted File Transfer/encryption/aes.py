from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import base64

def pad(data):
    return data + b' ' * (16 - len(data) % 16)

def encrypt_aes(data):
    key = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_ECB)
    enc = cipher.encrypt(pad(data))
    return enc, base64.b64encode(key)

def decrypt_aes(enc_data, b64_key):
    key = base64.b64decode(b64_key)
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.decrypt(enc_data).rstrip(b' ')
