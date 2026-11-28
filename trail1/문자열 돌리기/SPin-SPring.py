word = input()

print(word)

for _ in range(len(word)):
    word = word[-1] + word[:len(word)-1]
    print(word)