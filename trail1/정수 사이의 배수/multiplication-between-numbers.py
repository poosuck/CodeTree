A, B = map(int, input().split())

ans = 0
cnt = 0

for i in range(A, B+1):
    if (i % 5 == 0) or (i % 7 == 0):
        ans += i
        cnt += 1

ans_sum = ans
ans_average = ans/cnt

print(f'{ans_sum} {ans_average:.1f}')