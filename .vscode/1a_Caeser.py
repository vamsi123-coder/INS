#Caeser_Cipher

def caesar_encrypt(text, s):
    result = ""

    for char in text:
        if char.isupper():
            result += chr((ord(char) + s - 65) % 26 + 65)
        elif char.islower():
            result += chr((ord(char) + s - 97) % 26 + 97)
        else:
            result += char

    return result


def caesar_decrypt(text, s):
    return caesar_encrypt(text, -s)


text = input("Enter plain text: ")
s = int(input("Enter shift key: "))

encrypted = caesar_encrypt(text, s)

print("Encrypted text:", encrypted)
print("Decrypted text:", caesar_decrypt(encrypted, s))
