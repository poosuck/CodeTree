N = int(input())

i = 0
cnt = 0

while N > 1:
    i += 1
    cnt += 1
    N //= i


print(cnt)