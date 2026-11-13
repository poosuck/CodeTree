n = int(input())
segments = [tuple(map(int, input().split())) for _ in range(n)]

# Please write your code here.
OFFSET = 100
lst = [0] * 201

for i, j in segments:
    start = min(i, j)
    end = max(i, j)

    for idx in range(start, end+1):
        lst[idx] += 1

print(max(lst))