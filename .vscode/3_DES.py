
from Crypto.Cipher import DES
from Crypto.Util.Padding import pad, unpad
import binascii

def des_encrypt(message, key):
    cipher = DES.new(key, DES.MODE_ECB)
    return cipher.encrypt(pad(message.encode(), 8))


def des_decrypt(ciphertext, key):
    cipher = DES.new(key, DES.MODE_ECB)
    return unpad(cipher.decrypt(ciphertext), 8).decode()


secret_key = b'8bytekey'
message = "Hello, this is a secret message!"

print("Original Message:", message)
print("Secret Key:", secret_key.decode())

encrypted = des_encrypt(message, secret_key)

print("Encrypted (Hex):",
      binascii.hexlify(encrypted).decode())

decrypted = des_decrypt(encrypted, secret_key)

print("Decrypted Message:", decrypted)
