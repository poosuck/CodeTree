n = int(input())
lst = list(map(int, input().split()))
lst = lst[::-1]

min_num = float('inf')
for i in range(n):
    for j in range(i+1, n):
        if abs(lst[i] - lst[j]) < min_num:
            min_num = abs(lst[i] - lst[j])

print(min_num)