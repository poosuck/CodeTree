A = input()

ans = ''

for i in range(1, len(A), 2):
    ans += A[i]

ans = ans[::-1]
print(ans)