def is_three(num, ans):
    cnt = 0
    for i in range(1, num + 1):
        if num % i == 0:
            cnt += 1
    if cnt == 3:
        ans += 1

    return ans


start, end = map(int, input().split())
ans = 0
# Please write your code here.

for num in range(start, end + 1):
    ans = is_three(num, ans)

print(ans)