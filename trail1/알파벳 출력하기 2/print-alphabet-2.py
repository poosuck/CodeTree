n = int(input())

num = 65
for i in range(n):
    print('  ' * i, end='')
    for j in range(n-i):
        print(chr(num), end=' ')
        num += 1
        if num == 91:
            num = 65
    print()