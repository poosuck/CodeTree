N = int(input())

nums = []
for _ in range(N):
    nums.append(int(input()))

ans = 0
for i in nums:
    if (
        i % 2 == 1
        and i % 3 == 0
    ):
        ans += i

print(ans)