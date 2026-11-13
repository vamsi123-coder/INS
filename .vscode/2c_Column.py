
text = input("Enter text: ")
key = input("Enter key: ")

cols = len(key)

while len(text) % cols != 0:
    text += 'X'

rows = len(text) // cols

matrix = [
    list(text[i*cols:(i+1)*cols])
    for i in range(rows)
]

order = sorted(range(cols), key=lambda i: key[i])

cipher = ""

for j in order:
    for i in range(rows):
        cipher += matrix[i][j]

print("Encrypted:", cipher)

matrix = [[""]*cols for _ in range(rows)]
k = 0

for j in order:
    for i in range(rows):
        matrix[i][j] = cipher[k]
        k += 1

plain = ""

for i in range(rows):
    plain += "".join(matrix[i])

print("Decrypted:", plain.rstrip('X'))
