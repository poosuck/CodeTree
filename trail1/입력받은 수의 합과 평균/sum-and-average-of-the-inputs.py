N = int(input())

nums = []
for _ in range(N):
    nums.append(int(input()))

print(f'{sum(nums)} {sum(nums) / len(nums):.1f}')