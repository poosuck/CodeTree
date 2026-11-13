N = int(input())
A = list(map(int, input().split()))

# Please write your code here.


def cow(arr, idx, depth):

    global cnt
    # 가지치기

    # 종료조건
    if depth == 3:
        cnt += 1
        return

    # 진행할 작업

    for i in range(idx+1, N):
        if A[i] >= A[idx]:
            # 재귀 호출
            cow(A, i, depth+1)


cnt = 0

for i in range(N):
    cow(A, i, 1)

print(cnt)

