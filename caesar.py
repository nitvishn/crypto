key=int(input("Key: "))
plaintext=input("Plaintext: ")

ciphertext=""

for char in plaintext:
	outchar=ord(char.lower())-97
	outchar+=key
	outchar%=26
	ciphertext+=chr(outchar+97)

print('Ciphertext: '+ciphertext)