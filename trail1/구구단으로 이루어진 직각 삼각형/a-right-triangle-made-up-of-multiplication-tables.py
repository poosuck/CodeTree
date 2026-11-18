n = int(input())+1

for i in range(1, n):
    for j in range(1, n - i+1):
        if j == n-i:
            print(f'{i} * {j} = {i*j}', end='')
        else:
            print(f'{i} * {j} = {i*j}', end=' / ')
    print()