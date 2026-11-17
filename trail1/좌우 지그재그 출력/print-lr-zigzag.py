n = int(input())
cnt = 0

for i in range(1, n+1):
    if i % 2 == 1:
        for _ in range(1, n+1):
            cnt += 1
            print(cnt, end=' ')
        print()

    else:
        cnt += n
        for _ in range(1, n+1):
            print(cnt, end=' ')
            cnt -= 1
        print()
        cnt += n