n = int(input())

for i in range(n):
    line = ''

    for j in range(n):
        if i == 0 or (j % 2 == 1 and j >= i):
            line += '* '
        else:
            line += '  '

    if '*' in line:
        print(line.rstrip())