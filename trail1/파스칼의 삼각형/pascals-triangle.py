n = int(input())

semo = []

# 모든 값이 1인 세모 하나 생성
for i in range(n):
    semo.append([1] * (i + 1))

# 세모[i][j]값 = 좌상단 + 상단 값
# 실질적으로 모서리부분은 변하지 않기 때문에
# 행은 인덱스 2부터, 열은 인덱스 1부터 행까지만 변경

for row in range(2, n):
    for col in range(1, row):
        semo[row][col] = semo[row - 1][col - 1] + semo[row - 1][col]

for i in semo:
    for j in i:
        print(j, end=' ')
    print()
