myfile = open("words.txt")

def numberofwords(myfile):
	for words in myfile:
		letters = words.strip()
		if len(letters) > 20:
			print(letters)
numberofwords(myfile)
