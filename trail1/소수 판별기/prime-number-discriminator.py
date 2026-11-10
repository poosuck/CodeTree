n = int(input())

ans = 'P'
for i in range(2, n):
    if n % i == 0:
        ans = 'C'
        break

print(ans)