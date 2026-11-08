A, B = map(int, input().split())

ans = 0
for i in range(min(A, B), max(A, B)+1):
    if i % 5 == 0:
        ans += i

print(ans)