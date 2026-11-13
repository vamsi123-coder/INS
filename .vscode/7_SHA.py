
import hashlib

message = input("Enter message: ")

sha256_hash = hashlib.sha256(
    message.encode("utf-8")
).hexdigest()

print("Message:", message)

print("SHA-256 Hash:", sha256_hash)

print("Hash length:", len(sha256_hash),
      "hex characters")
