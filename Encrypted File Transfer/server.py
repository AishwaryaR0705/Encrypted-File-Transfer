import socket
from encryption.aes import decrypt_aes
from encryption.fernet_encryptor import decrypt_fernet
from utils.checksum import sha256_checksum

def start_server(host="0.0.0.0", port=9999):
    s = socket.socket()
    s.bind((host, port))
    s.listen(1)
    print(f"🔌 Server listening on {host}:{port}...")

    conn, addr = s.accept()
    print(f"📥 Connection from {addr}")

    data = b""
    while True:
        chunk = conn.recv(4096)
        if not chunk:
            break
        data += chunk
    conn.close()

    enc_data, key_checksum = data.split(b"<END>")
    key, checksum = key_checksum.split(b"<KEY>")

    # Try AES decryption
    try:
        decrypted = decrypt_aes(enc_data, key)
    except:
        decrypted = decrypt_fernet(key, enc_data)

    with open("received_file", "wb") as f:
        f.write(decrypted)

    print("✅ File received and saved.")
    print("Received Checksum:", checksum.decode())
    print("Computed Checksum:", sha256_checksum(decrypted))

if __name__ == "__main__":
    start_server()
