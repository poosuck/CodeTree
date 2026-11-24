arr = [list(map(int, input().split())) for _ in range(4)]

ans = 0

# 가로 순회
for i in range(4):
    # 세로는 순회중인 가로 인덱스까지만 순회
    # 가로: 1 -> 세로는 1까지, 가로:2 -> 세로도 2까지
    for j in range(i + 1):
        ans += arr[i][j]

print(ans)