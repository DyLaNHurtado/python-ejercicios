def getLetters(word):    
    return word[0].upper()+word[1:-1].lower()+word[-1].upper()

print(getLetters("ayuda"))