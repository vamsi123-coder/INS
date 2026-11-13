
def diffie_hellman(p, g, a, b):

    A = pow(g, a, p)
    B = pow(g, b, p)

    alice_key = pow(B, a, p)
    bob_key = pow(A, b, p)

    print("Public prime (p):", p)
    print("Public base (g):", g)

    print("Alice public key:", A)
    print("Bob public key:", B)

    print("Alice shared secret:", alice_key)
    print("Bob shared secret:", bob_key)

    print("Keys match:", alice_key == bob_key)


p = 23
g = 5
a = 6
b = 15

diffie_hellman(p, g, a, b)
