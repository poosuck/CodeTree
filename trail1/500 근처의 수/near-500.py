lst = list(map(int, input().split()))

# 500이하 최댓값: -무한
# 500이상 최솟값: 무한
under_500 = float('-inf')
up_500 = float('inf')

# 리스트 순회
for i in lst:
    # 숫자가 500 초과일때
    if i > 500:
        # 현재의 500이상 최솟값보다 작으면 갱신
        if i < up_500:
            up_500 = i
    
    # 숫자가 500 미만일때
    elif i < 500:
        # 현재의 500미만 최댓값보다 크면 갱신
        if i > under_500:
            under_500 = i


print(under_500, up_500)