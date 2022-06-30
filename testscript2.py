#create a function that removes duplicates from a list
def duplicateremove(listx):
	blanklist = []
	for i in listx:
		if i not in blanklist:
			blanklist.append(i)
	return blanklist

#create a function to take a string of numbers and sum them
def stringsum(string):
	sumstring = 0
	for i in string:
		if i.isdigit():
			sumstring += int(i)
	return sumstring

#create a caesar cipher function
def caesarcipher(message):
	cipher = ""
	for char in message:
		if not char.isalpha():
			continue
		up = char.upper()
		charnum = ord(up) + 1
		if charnum > ord("Z"):
			charnum = ord("A")
		cipher += chr(charnum)
	return cipher

#create a function that reverses the caesar cipher
def revcaesarcipher(cipher):
	message = ""
	for char in cipher:
		charnum = ord(char) - 1
		if charnum < ord("A"):
			charnum = ord("Z")
		message += chr(charnum)
	return message
