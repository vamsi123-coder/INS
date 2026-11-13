
import hashlib

p = 23
q = 11
g = 2

# Private key and public key
x = 3
y = pow(g, x, p)

# Hash function
def H(message):
    return int(hashlib.sha256(message.encode()).hexdigest(), 16)


# Generate digital signature
def sign(message, k):
    z = H(message) % q

    r = pow(g, k, p) % q

    k_inv = pow(k, -1, q)

    s = (k_inv * (z + x*r)) % q

    return r, s


# Verify digital signature
def verify(message, signature):
    r, s = signature

    if not (0 < r < q and 0 < s < q):
        return False

    z = H(message) % q

    w = pow(s, -1, q)

    u1 = (z*w) % q
    u2 = (r*w) % q

    v = (pow(g, u1, p) *
         pow(y, u2, p) % p) % q

    return v == r


message = "Digital Signature"
k = 2

signature = sign(message, k)

print("Message:", message)
print("Public key:", y)
print("Signature (r, s):", signature)
print("Verification:", verify(message, signature))
