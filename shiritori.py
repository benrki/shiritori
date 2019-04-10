import re

print "Shiritori game cheater"
letter = "true"
while letter:
	try:
		letter = raw_input("Enter letter: ")
	except EOFError:
		print "\n"
		break
	if not letter.isalpha():
		break
	dictionary = open("dictionary", "r")
	for word in dictionary:
		if word.startswith(letter):
			print word.strip()
	print "------------------------"