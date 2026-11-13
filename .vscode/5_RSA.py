
def power(base, exp, m):
    result = 1

    while exp:
        if exp & 1:
            result = result * base % m

        base = base * base % m
        exp //= 2

    return result


def gcd(a, b):
    while b:
        a, b = b, a % b

    return a


def modInverse(e, phi):
    for d in range(2, phi):
        if e*d % phi == 1:
            return d

    return -1


def generateKeys():
    p, q = 7919, 1009

    n = p*q
    phi = (p-1)*(q-1)

    for e in range(2, phi):
        if gcd(e, phi) == 1:
            break

    d = modInverse(e, phi)

    return e, d, n


def encrypt(m, e, n):
    return power(m, e, n)


def decrypt(c, d, n):
    return power(c, d, n)


e, d, n = generateKeys()

print("Public Key:", (e, n))
print("Private Key:", (d, n))

M = 123

print("Original Message:", M)

C = encrypt(M, e, n)

print("Encrypted Message:", C)
print("Decrypted Message:", decrypt(C, d, n))
