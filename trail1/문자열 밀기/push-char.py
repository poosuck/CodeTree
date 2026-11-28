def shift(word):
    word = word[1:] +  word[0]
    return word


word = input()

print(shift(word))