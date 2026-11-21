n = int(input())

lst = list(map(int, input().split()))

# 리스트에서 짝수 요소만 별도의 리스트에 저장
ans = []
for i in lst:
    if i % 2 == 0:
        ans.append(i)

# 리스트 역순으로 바꿔서 출력
for i in ans[::-1]:
    print(i, end=' ')