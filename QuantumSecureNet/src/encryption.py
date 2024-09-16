from Crypto.Cipher import AES
from Crypto.Random import get_random_bytes
import hashlib

def aes_encrypt(data, key):
    key = hashlib.sha256(key.encode()).digest()
    iv = get_random_bytes(16)
    cipher = AES.new(key, AES.MODE_CBC, iv)
    padding_length = 16 - len(data) % 16
    data += chr(padding_length) * padding_length
    ciphertext = cipher.encrypt(data.encode())
    return iv + ciphertext

def aes_decrypt(ciphertext, key):
    key = hashlib.sha256(key.encode()).digest()
    iv = ciphertext[:16]
    cipher = AES.new(key, AES.MODE_CBC, iv)
    decrypted_data = cipher.decrypt(ciphertext[16:])
    padding_length = decrypted_data[-1]
    return decrypted_data[:-padding_length].decode()

if __name__ == "__main__":
    data = "This is sensitive data."
    key = "supersecretquantumkey"
    encrypted_data = aes_encrypt(data, key)
    print(f"Encrypted Data: {encrypted_data}")
    decrypted_data = aes_decrypt(encrypted_data, key)
    print(f"Decrypted Data: {decrypted_data}")
