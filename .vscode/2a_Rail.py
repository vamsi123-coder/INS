
def encrypt(text, key):
    rail = ["" for _ in range(key)]
    row, d = 0, 1

    for ch in text:
        rail[row] += ch

        if row == 0:
            d = 1
        elif row == key-1:
            d = -1
        row += d
    return "".join(rail)


def decrypt(cipher, key):
    pos = [[0]*len(cipher) for _ in range(key)]
    row, d = 0, 1

    for i in range(len(cipher)):
        pos[row][i] = 1

        if row == 0:
            d = 1
        elif row == key-1:
            d = -1
        row += d

    rail = [[""]*len(cipher) for _ in range(key)]
    k = 0

    for i in range(key):
        for j in range(len(cipher)):
            if pos[i][j]:
                rail[i][j] = cipher[k]
                k += 1

    result = ""
    row, d = 0, 1

    for i in range(len(cipher)):
        result += rail[row][i]
        if row == 0:
            d = 1
        elif row == key-1:
            d = -1
        row += d
    return result


text = input("Enter text: ")
key = int(input("Enter key: "))

c = encrypt(text, key)

print("Encrypted:", c)
print("Decrypted:", decrypt(c, key))
