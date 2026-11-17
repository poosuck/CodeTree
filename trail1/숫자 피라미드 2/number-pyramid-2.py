n = int(input()) + 1
cnt = 0

for i in range(1, n):
    for j in range(1, i+1):
        cnt += 1
        print(cnt, end=' ')
    print()