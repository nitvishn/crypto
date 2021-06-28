key = int(input("Key: "))


def caesar(plaintext):
    ciphertext = ""

    for char in plaintext:
        if not char.isalpha():
            ciphertext += char
            continue
        outchar = ord(char.lower()) - 97
        outchar += key
        outchar %= 26
        ciphertext += chr(outchar + 97)
    return ciphertext


while True:
    plaintext = input("Plaintext: ")
    print('Ciphertext: ' + caesar(plaintext))
