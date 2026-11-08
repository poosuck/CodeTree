nums = []
ans = 0
cnt = 0

for i in range(10):
    nums.append(int(input()))

for num in nums:
    if 0 <= num <= 200:
        ans += num
        cnt += 1

ans_sum = ans
ans_average = ans / cnt

print(f'{ans_sum} {ans_average:.1f}')