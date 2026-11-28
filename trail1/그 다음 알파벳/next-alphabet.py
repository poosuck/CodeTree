def next_alp(char):
    num = ord(char)

    if num == 122:
        num = 97
    else:
        num += 1

    return chr(num)


char = input()

print(next_alp(char))