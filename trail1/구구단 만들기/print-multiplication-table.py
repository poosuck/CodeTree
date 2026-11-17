a, b = map(int, input().split())

nums = []
for i in range(b, a-1, -1):
    if i % 2 == 0:
        nums.append(i)





for i in range(1, 10):
    for j in nums:
        if j == nums[-1]:
            print(f'{j} * {i} = {i*j}', end=' ')
        else:
            print(f'{j} * {i} = {i*j}', end=' / ')
    print()