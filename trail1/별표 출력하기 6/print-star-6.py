def star(n):

    for i in range(n*2-1):

        print('*', end=' ')
    print()



n = int(input())

for i in range(n, 0, -1):
    print('  ' * (n - i), end='')
    star(i)

for i in range(2, n+1):
    print('  ' * (n - i), end='')
    star(i)

