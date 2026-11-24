def move(row, col):
    global cnt

    while 0 <= row < N and 0 <= col < M:
        arr[row][col] = cnt
        cnt += 1
        row += 1
        col -= 1


N, M = map(int, input().split())

# Please write your code here.
arr = [[0] * M for _ in range(N)]
cnt = 1

for col in range(M):
    move(0, col)

for row in range(1, N):
    move(row, M-1)

for i in arr:
    for j in i:
        print(j, end=' ')
    print()