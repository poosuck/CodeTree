n = int(input())
A = list(map(int, input().split()))

# Please write your code here.
total = float('inf')

# 모이는 집 번호
for i in range(n):
    # 모이는 집이 바뀔때마다 값 초기화해서
    # 이동 거리 다시 계산
    new_total = 0


    for j in range(n):
        # 집에 있는 인원 수 * 거리 누적 합
        new_total += A[j] * abs(i - j)
        # 구한 누적합이 현재 합 보다 작으면 갱신
    if new_total < total:
        total = new_total

print(total)