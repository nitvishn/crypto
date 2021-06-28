keyString=input("Key: ")
plaintext=input("Plaintext: ")

ciphertext=""

for i in range(len(keyString))

for i in range(len(plaintext)):
	char=plaintext[i]
	if(not(char.isalpha())):
		ciphertext+=char
		continue
	key=ord(keyString[i%len(keyString)].lower())-97
	outchar=ord(char.lower())-97
	outchar+=key
	outchar%=26
	ciphertext+=chr(outchar+97)

print('Ciphertext: '+ciphertext)
