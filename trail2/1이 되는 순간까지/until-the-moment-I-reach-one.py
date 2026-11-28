N = int(input())

# Please write your code here.
cnt = 0

def f(n):
    global cnt

    if n == 1:
        return

    cnt += 1

    if n % 2 == 0:
        f(n // 2)
    
    else:
        f(n // 3)

f(N)
print(cnt)