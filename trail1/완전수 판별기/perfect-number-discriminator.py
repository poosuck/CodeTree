def is_완전수(N):
    num = 0
    for i in range(1, N):
        if N % i == 0:
            num += i
    
    if num == N:
        print('P')
    else:
        print('N')


N = int(input())
is_완전수(N)