arr = [list(map(int, input().split())) for _ in range(2)]

# 가로 평균
for i in arr:
    print(sum(i) / 4, end=' ')
print()

# 세로 평균
for j in range(4):
    ans = 0
    for i in range(2):
        ans += arr[i][j]
    print(ans / 2, end=' ')
print()

# 전체 평균
ans = 0
for i in arr:
    for j in i:
        ans += j
print(f'{ans / 8:.1f}')