n = int(input())

nums = []
for _ in range(n):
    i, j = map(int, input().split())
    nums.append((i, j))

total = 0

for i, j in nums:
    for num in range(i, j+1):
        if num % 2 == 0:
            total += num

    print(total)
    total = 0