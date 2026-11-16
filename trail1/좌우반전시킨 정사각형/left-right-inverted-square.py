n = int(input())

for row in range(1, n+1):
    for col in range(n, 0, -1):
        print(col * row, end=' ')
    print()