a, b = map(int,input().split())
idx = [0] * 10

ans = 0
while a > 1:
    a, left = a // b, a % b
    idx[left] += 1

for i in idx:
    ans += i**2
print(ans)