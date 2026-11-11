n = int(input())

for i in range(n, 0, -1):
    for j in range(n - i):
        print(' ', end=' ')
    print('* ' * (2 * i - 1))
    