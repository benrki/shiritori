import urllib2, re, string
print "Creating dictionary..."
alphabet = list(string.ascii_lowercase)
dictionary = open("dictionary", "w")
for letter in alphabet:
	response = urllib2.urlopen('http://words-that-start-with-%c.worddetector.com/p/%c*/' %(letter, letter))
	html = response.read()
	words = re.findall('>%c.+<' %letter, html)
	
	fWords = []
	for word in words:
		word = word.lstrip('>')
		word = word.rstrip('</a><')
		fWords.append(word)
	fWords.reverse()
	
	for i in range (0, 30):
		dictionary.write(fWords[i] + "\n")
	printf letter + " "
dictionary.close()
