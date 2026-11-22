lst = list(map(int, input().split()))

odd_idx = 0
even_idx = 0

for i in range(len(lst)):
    if i % 2 == 0:
        even_idx += lst[i]
    else:
        odd_idx += lst[i]

ans = max(odd_idx, even_idx) - min(odd_idx, even_idx)
print(ans)