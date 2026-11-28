def f(n):
    if n == 1:
        return 1
    
    return f(n-1) * n


N = int(input())

# Please write your code here.
print(f(N))