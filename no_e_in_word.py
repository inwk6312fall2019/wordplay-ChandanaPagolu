myfile = open ("words.txt")
def no_e_in_word(word):
	for char in word:
        	if char in 'Ee':
	            	return False
	return True

count = 0
for letter in myfile:
    word = letter.strip()
    if no_e_in_word(word):
        count += 1
        print (word)

percent = (count / 113809.0) * 100

print (str(percent) + "% of the words don't have an 'e'.")
