def make(n):
    for i in range(1, n*2):
        if i > (n * 2) // 2:
            print('@ ' * (n*2-i))

        elif i == n * 2 // 2:
            print('@ ' * n, end=' ')
            print()

        else:
            print('  ' * (n - i), end='')
            print('@ ' * i)


num = int(input())
make(num)
