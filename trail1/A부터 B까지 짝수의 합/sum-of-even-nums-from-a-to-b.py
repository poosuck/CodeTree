A, B = map(int, input().split())

ans = 0
start = min(A, B)
end = max(A, B) + 1

for i in range(start, end):
    if i % 2 == 0:
        ans += i

print(ans)