
import numpy as np

def encrypt(K, pt):
    pt = pt.upper().replace(" ", "")

    while len(pt) % 3 != 0:
        pt += "X"

    ct = ""

    for i in range(0, len(pt), 3):
        P = np.array([ord(ch)-65 for ch in pt[i:i+3]])
        C = np.dot(K, P) % 26
        ct += "".join(chr(int(x)+65) for x in C)

    return ct


key = input("Enter Key (9 chars): ").upper()

K = np.array([ord(ch)-65 for ch in key]).reshape(3, 3)

pt = input("Enter plaintext: ").upper()

print("Key Matrix:")
print(K)

print("Ciphertext:", encrypt(K, pt))
