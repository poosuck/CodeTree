def poppop(word):
    word.pop(-2)
    word.pop(1)

    return ''.join(word)


word = list(input())

print(poppop(word))