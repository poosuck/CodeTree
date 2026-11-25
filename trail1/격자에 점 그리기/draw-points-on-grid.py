n, m = map(int, input().split())

arr = [[0] * n for _ in range(n)]
cnt = 1

for _ in range(m):
    row, col = tuple(map(int, input().split()))

    arr[row-1][col-1] = cnt
    cnt += 1

for i in arr:
    for j in i:
        print(j, end=' ')
    print()