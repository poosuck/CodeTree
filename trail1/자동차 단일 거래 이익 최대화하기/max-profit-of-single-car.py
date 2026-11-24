n = int(input())
price = list(map(int, input().split()))

# Please write your code here.

# 최대 차액 0으로 설정
max_price = 0

# 리스트 n번째 요소 선택
for buy in range(n):
    # 리스트의 n+1번째 요소 선택
    for sell in range(buy+1, n):
        
        # 차액이 현재 최대 차액보다 크고
        # 0 이상이면 갱신
        if price[sell] - price[buy] > max_price:
            if price[sell] - price[buy] > 0:
                max_price = price[sell] - price[buy]


print(max_price)