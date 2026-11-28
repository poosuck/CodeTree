def before_alp(char):
    num = ord(char)

    if num == 97:
        num = 122
    else:
        num -= 1

    return chr(num)


char = input()

print(before_alp(char))