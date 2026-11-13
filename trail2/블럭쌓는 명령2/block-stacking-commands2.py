n, k = map(int, input().split())
commands = [tuple(map(int, input().split())) for _ in range(k)]

blocks = [0] * (n+1)
# Please write your code here.
for i, j in commands:
    start = min(i, j)
    end = max(i, j)

    for idx in range(start, end+1):
        blocks[idx] += 1

print(max(blocks))