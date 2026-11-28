n, m = map(int, input().split())
arr = list(map(int, input().split()))
queries = [tuple(map(int, input().split())) for _ in range(m)]

# Please write your code here.

def solve(queries):
    global arr

    for start, end in queries:
        print(sum(arr[start-1:end]))

solve(queries)