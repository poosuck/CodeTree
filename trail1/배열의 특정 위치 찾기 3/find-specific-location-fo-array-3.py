lst = list(map(int, input().split()))

# 정답 저장할 변수 생성
ans = 0

# 리스트 순회하기
for i in range(len(lst)):
    # 리스트의 i번째 요소가 0이라면
    if lst[i] == 0:
        # 앞에 3개 수 더하기
        for j in range(i-1, i-4, -1):
            ans += lst[j]
        # 더이상 리스트를 순회하면서 0을 찾을 필요가 없으니까 중단
        break

print(ans)