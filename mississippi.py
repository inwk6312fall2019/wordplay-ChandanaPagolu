def triple_double(word):
    i = 0
    count = 0
    while i < len(word) - 1:
        if word[i] == word[i + 1]:
            count = count + 1
            if count == 3:
                return True
            i = i + 2
        else:
            i = i + 1 - 2 * count
            count = 0
    return False


def find_triple_double():
    myfile = open('words.txt')
    for line in myfile:
        word = line.strip()
        if triple_double(word):
            print(word)


print('Here are all the words in the list that have')
print('three consecutive double letters.')
find_triple_double()
print('')

