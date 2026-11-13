n = int(input())
commands = [tuple(input().split()) for _ in range(n)]
x = []
dir = []
for num, direction in commands:
    x.append(int(num))
    dir.append(direction)


now = 100000
color = ['0'] * 200001
white = [0] * 200001
black = [0] * 200001

for i in range(n):
    if dir[i] == 'L':
        for _ in range(x[i]):
            color[now] = 'W'
            white[now] += 1
            now -= 1
        now += 1

    else:
        for _ in range(x[i]):
            color[now] = 'B'
            black[now] += 1
            now += 1
        now -= 1

gray_cnt = 0
white_cnt = 0
black_cnt = 0

for i in range(200001):
    if white[i] >= 2 and black[i] >= 2:
        color[i] = 'G'

    if color[i] == 'W':
        white_cnt += 1
    elif color[i] == 'B':
        black_cnt += 1
    elif color[i] == 'G':
        gray_cnt += 1

print(white_cnt, black_cnt, gray_cnt)
