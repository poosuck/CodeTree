char = input()

chars = ['L', 'E', 'B', 'R', 'O', 'S']

if char not in chars:
    print(None)
else:
    print(chars.index(char))