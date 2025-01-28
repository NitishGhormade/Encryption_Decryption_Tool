from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import base64

def encrypt(key, plaintext):
    cipher = AES.new(key.encode(), AES.MODE_CBC, iv=b"1234567890123456")
    encrypted = cipher.encrypt(pad(plaintext.encode(), AES.block_size))
    return base64.b64encode(encrypted).decode()

def decrypt(key, encrypted_text):
    cipher = AES.new(key.encode(), AES.MODE_CBC, iv=b"1234567890123456")
    decrypted = unpad(cipher.decrypt(base64.b64decode(encrypted_text)), AES.block_size)
    return decrypted.decode()

if __name__ == "__main__":
    secret_key = input("Enter a 16-character key: ")
    message = input("Enter the message: ")
    
    encrypted_message = encrypt(secret_key, message)
    print(f"Encrypted: {encrypted_message}")
    
    decrypted_message = decrypt(secret_key, encrypted_message)
    print(f"Decrypted: {decrypted_message}")
