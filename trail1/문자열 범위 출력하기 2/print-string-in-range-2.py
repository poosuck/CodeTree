word = input()
num = int(input())

word = word[::-1]

if len(word) < num:
    print(word)

else:
    print(word[:num])
    