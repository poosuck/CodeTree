n, m = map(int, input().split())

# Please write your code here.

cnt = 0
arr = [[0] * m for _ in range(n)]

# n: row
# m: col

for col in range(m):
    if col % 2 == 0:
        for row in range(n):
            arr[row][col] = cnt
            cnt += 1
    else:
        for row in range(n-1, -1, -1):
            arr[row][col] = cnt
            cnt += 1


for i in arr:
    for j in i:
        print(j, end=' ')
    print()