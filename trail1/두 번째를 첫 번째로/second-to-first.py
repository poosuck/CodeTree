word = list(input())

same_char = word[1]
target_char = word[0]

for i in range(len(word)):
    if word[i] == same_char:
        word[i] = target_char

print(''.join(word))