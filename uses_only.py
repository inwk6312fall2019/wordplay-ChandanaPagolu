def uses_only(word, letter):
    for character in word:
        if character not in letter:
            return False
    return True

