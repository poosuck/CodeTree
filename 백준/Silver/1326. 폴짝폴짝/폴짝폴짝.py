from collections import deque

# 징검다리개수
n = int(input())
# 다리에 쓰인 수
lst = list(map(int, input().split()))
# 시작, 끝 위치
start, end = map(int, input().split())

start -= 1
end -= 1


def jump(start, end):
    q = deque()
    visited = [False] * n
    q.append((start, 0))
    visited[start] = True

    while q:
        start, jump_cnt = q.popleft()
        step = lst[start]

        if start == end:
            return jump_cnt

        for i in range(start + step, n, step):
            if not visited[i]:
                visited[i] = True
                q.append((i, jump_cnt + 1))

        for i in range(start - step, -1, -step):
            if not visited[i]:
                visited[i] = True
                q.append((i, jump_cnt + 1))

    return -1


print(jump(start, end))