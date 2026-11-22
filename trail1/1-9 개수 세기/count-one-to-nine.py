n = int(input())

nums = list(map(int, input().split()))
lst = [0] * 10

for idx in nums:
    lst[idx] += 1

for i in lst[1:]:
    print(i)