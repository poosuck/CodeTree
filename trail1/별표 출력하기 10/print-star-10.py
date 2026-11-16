N = int(input())

# 윗부분
for i in range(1, N + 1):
    if i % 2 == 1:
        print('* ' * ((i + 1) // 2))
    else:
        print('* ' * (N + 1 - i // 2))

# 아랫부분
for i in range(N, 0, -1):
    if i % 2 == 1:
        print('* ' * ((i + 1) // 2))
    else:
        print('* ' * (N + 1 - i // 2))