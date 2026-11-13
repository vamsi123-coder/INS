
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad, unpad
import binascii

def aes_encrypt(message, key):
    cipher = AES.new(key, AES.MODE_ECB)
    return cipher.encrypt(pad(message.encode(), AES.block_size))


def aes_decrypt(ciphertext, key):
    cipher = AES.new(key, AES.MODE_ECB)
    return unpad(
        cipher.decrypt(ciphertext),
        AES.block_size
    ).decode()


secret_key = b'1234567890123456'
message = "Hello, this is a secret message!"

print("Original Message:", message)
print("Secret Key:", secret_key.decode())

encrypted = aes_encrypt(message, secret_key)

print("Encrypted (Hex):",
      binascii.hexlify(encrypted).decode())

decrypted = aes_decrypt(encrypted, secret_key)

print("Decrypted Message:", decrypted)
