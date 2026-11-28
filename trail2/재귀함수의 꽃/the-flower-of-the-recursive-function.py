def abc(N):
    if N == 0:
        return
    
    print(N, end=' ')
    abc(N-1)
    print(N, end=' ')


N = int(input())
# Please write your code here.
abc(N)