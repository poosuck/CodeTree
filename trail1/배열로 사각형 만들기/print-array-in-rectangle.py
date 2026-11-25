# 가로 세로 길이 5인 배열에 1 채우기
# 가로, 세로 인덱스가 0인 부분을 제외한
# 배열[1][1]부터 순회하면서 더해서 출력

arr = [[1] * 5 for _ in range(5)]

for row in range(1, 5):
    for col in range(1, 5):
        arr[row][col] = arr[row-1][col] + arr[row][col-1]


for lst in arr:
    for idx in lst:
        print(idx, end=' ')
    print()