def f(n):
    if n < 0:
        return 0
    if n % 2 == 1:
        return n + f(n-2)
    elif n % 2 == 0:
        return n + f(n-2)


N = int(input())

# Please write your code here.
print(f(N))