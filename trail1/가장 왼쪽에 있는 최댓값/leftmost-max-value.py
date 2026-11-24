n = int(input())
a = list(map(int, input().split()))

# Please write your code here.


num = 0

# 인덱스가 1이 될때까지 반복
while num != 1:
    # 리스트 순회하면서 최댓값 인덱스 출력
    num = a.index(max(a))+1
    print(num, end=' ')
    # 최댓값 인덱스 포함 뒤에 다 날리기
    a = a[:num-1]

