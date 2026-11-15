n = int(input())

for i in range(2*n + 1):
    if i % 2 == 1:
        print('*   ' * ((2*n + 2) // 2))
    else:
        print('* ' * (2*n + 1))