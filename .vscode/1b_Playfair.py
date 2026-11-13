
def create_matrix(key):
    key = key.lower().replace('j', 'i')
    chars = ""

    for ch in key + "abcdefghiklmnopqrstuvwxyz":
        if ch.isalpha() and ch not in chars:
            chars += ch

    return [list(chars[i:i+5]) for i in range(0, 25, 5)]


def prepare(text):
    text = text.lower().replace('j', 'i')
    text = ''.join(c for c in text if c.isalpha())

    result = ""
    i = 0

    while i < len(text):
        a = text[i]

        if i + 1 < len(text):
            b = text[i+1]

            if a == b:
                result += a + 'x'
                i += 1
            else:
                result += a + b
                i += 2
        else:
            result += a + 'z'
            i += 1

    if len(result) % 2 != 0:
        result += 'z'

    return result


def search(matrix, ch):
    if ch == 'j':
        ch = 'i'

    for i in range(5):
        for j in range(5):
            if matrix[i][j] == ch:
                return i, j


def encrypt(text, matrix):
    cipher = ""

    for i in range(0, len(text), 2):
        a, b = text[i], text[i+1]

        r1, c1 = search(matrix, a)
        r2, c2 = search(matrix, b)

        if r1 == r2:
            cipher += matrix[r1][(c1+1) % 5]
            cipher += matrix[r2][(c2+1) % 5]

        elif c1 == c2:
            cipher += matrix[(r1+1) % 5][c1]
            cipher += matrix[(r2+1) % 5][c2]

        else:
            cipher += matrix[r1][c2]
            cipher += matrix[r2][c1]

    return cipher


key = input("Enter Key: ")
text = input("Enter Plain Text: ")

matrix = create_matrix(key)
plain = prepare(text)

print("Key Matrix:")
for row in matrix:
    print(" ".join(row))

print("Prepared Plain Text:", plain)
print("Cipher Text:", encrypt(plain, matrix))
