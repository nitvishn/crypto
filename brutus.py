ciphertext = input("Ciphertext: ")

for k in range(26):
    plaintext = ""

    for char in ciphertext:
        if not char.isalpha():
            plaintext += char
            continue
        outchar = ord(char.lower()) - 97
        outchar += k
        outchar %= 26
        plaintext += chr(outchar + 97)

    print(k, ': ' + plaintext)
