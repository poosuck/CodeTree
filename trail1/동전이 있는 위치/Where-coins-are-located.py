n, coin = map(int, input().split())

arr = [[0] * n for _ in range(n)]

for _ in range(coin):
    row, col = tuple(map(int, input().split()))

    arr[row-1][col-1] = 1

for i in arr:
    for j in i:
        print(j, end=' ')
    print()