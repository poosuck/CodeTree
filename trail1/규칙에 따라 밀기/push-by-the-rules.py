def push(word, command):
    if command == 'L':
        return word[1:] + word[0]
    else:
        return word[-1] + word[:len(word)-1]


word = input()
commands = [i for i in input()]

for command in commands:
    word = push(word, command)

print(word)