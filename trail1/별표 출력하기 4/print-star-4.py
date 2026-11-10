n = int(input())
a = n
while n >= 1:
    print('* ' * n, end=' ')
    print()
    n -= 1

for i in range(2, a+1):
    print('* ' * i, end=' ')
    print()