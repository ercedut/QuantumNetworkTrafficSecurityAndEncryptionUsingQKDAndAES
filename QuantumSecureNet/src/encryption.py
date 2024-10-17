from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import hashlib

def aes_encrypt(data, key):
    key = hashlib.sha256(key.encode()).digest()
    cipher = AES.new(key, AES.MODE_CBC)
    ct_bytes = cipher.encrypt(pad(data.encode(), AES.block_size))
    return cipher.iv + ct_bytes

def aes_decrypt(ciphertext, key):
    key = hashlib.sha256(key.encode()).digest()
    iv = ciphertext[:16]
    ct = ciphertext[16:]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    data = unpad(cipher.decrypt(ct), AES.block_size)
    return data.decode()

if __name__ == "__main__":
    data = "This is sensitive data."
    key = "supersecretquantumkey"
    encrypted_data = aes_encrypt(data, key)
    print(f"Encrypted Data: {encrypted_data.hex()}")
    decrypted_data = aes_decrypt(encrypted_data, key)
    print(f"Decrypted Data: {decrypted_data}")
