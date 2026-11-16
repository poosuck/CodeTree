n = int(input())

if n == 1:
    print('*')

else:

    print('* ' * n)


    for i in range(1, n-1):
        
        print('* ' * i, end='')
        print('  ' * (n - i-1) + '*')
    print('* ' * n)


