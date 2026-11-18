n = int(input())
nums = [tuple(map(int, input().split())) for _ in range(n)]

# 총 합 저장할 변수
total = 1

# nums 리스트 순회
for num1, num2 in nums:
    # 숫자 a부터 b까지 반복하면서 total에 곱 더하기
    for i in range(num1, num2+1):
        total *= i
    # 튜플 하나 순회했으면 출력하고 합 초기화
    print(total)
    total = 1