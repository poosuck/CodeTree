n = int(input())
arr = list(map(int, input().split()))

# Please write your code here.
ans = arr[0]

def f(idx):
    global ans

    if idx == n-1:
        return arr[idx]
    
    return max(f(idx + 1), arr[idx])


print(f(0))