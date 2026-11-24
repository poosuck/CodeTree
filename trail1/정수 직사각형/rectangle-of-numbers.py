n, m = map(int, input().split())

cnt = 1
for row in range(n):
    for col in range(m):
        print(cnt, end=' ')
        cnt += 1
    print()