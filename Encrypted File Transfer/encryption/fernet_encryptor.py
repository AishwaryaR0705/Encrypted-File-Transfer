from cryptography.fernet import Fernet

def generate_fernet_key():
    return Fernet.generate_key()

def encrypt_fernet(key, data):
    return Fernet(key).encrypt(data)

def decrypt_fernet(key, encrypted_data):
    return Fernet(key).decrypt(encrypted_data)
