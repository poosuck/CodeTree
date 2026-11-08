A, B = map(int, input().split())

ans = 1

for i in range(A, B+1, A):
    ans *= i

print(ans)