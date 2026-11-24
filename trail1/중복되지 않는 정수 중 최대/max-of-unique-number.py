n = int(input())
nums = list(map(int, input().split()))

# Please write your code here.

# 리스트에 요소가 1개인것만 고르기
# 최댓값 출력

max_num = 0
for i in nums:
    if nums.count(i) == 1:
        if i > max_num:
            max_num = i

if max_num == 0:
    max_num = -1
    
print(max_num)
