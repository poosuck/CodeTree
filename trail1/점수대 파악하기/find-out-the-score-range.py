scores = list(map(int,input().split()))

for i in range(len(scores)):
    if scores[i] == 0:
        for j in range(i, len(scores)):
            scores = scores[:i]
        break
    else:
        scores[i] = scores[i] // 10


for i in range(100, 9, -10):
    print(f'{i} - {scores.count(i//10)}')
