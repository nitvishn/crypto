import random
import os
string=input("String: ")
bannedChars=[]
while(True):
	newString=""
	for char in string:
		if char in bannedChars:
			continue
		if(random.random()>0.5):
			newString+=char.upper()
		else:
			newString+=char.lower()
	print(newString)
	string=input("String: ")
	os.system('clear')
