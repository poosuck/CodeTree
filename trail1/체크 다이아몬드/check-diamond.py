def star(n):
    for i in range(1, 2*n):

        if i > n:
            print(' ' * (i - n), end='')
            print('* ' * (2*n - i))

        elif i == n:
            print('* ' * n)
    
        else:
            print(' ' * (n-i), end='')
            print('* ' * i)


n = int(input())
star(n)