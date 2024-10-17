from hashlib import sha256

def adjust_key_length(key):
    return sha256(key.encode()).digest()

def main():
    key = bb84_key_generation(128)
    print(f"Generated Key: {key}")
    
    aes_key = adjust_key_length(key)
    
    data = "This is sensitive data."
    print(f"Original Data: {data}")
    
    encrypted_data = aes_encrypt(data, aes_key)
    print(f"Encrypted Data: {encrypted_data.hex()}")
    
    real_packets = [encrypted_data.hex()]
    obfuscated_packets = generate_dummy_packets(real_packets, num_dummy=10)
    
    send_packets_with_random_delay(obfuscated_packets)
    
    decrypted_data = aes_decrypt(bytes.fromhex(real_packets[0]), aes_key)
    print(f"Decrypted Data: {decrypted_data}")

if __name__ == "__main__":
    main()
