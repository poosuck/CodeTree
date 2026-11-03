def compare(A, B):
    # a = 0, b = 0
    a = b = 0

    if A < B:
        a = 1
    else:
        a =0

    if A == B:
        b = 1
    else:
        b = 0
        
    print(a, b)


A, B = map(int, input().split())
compare(A, B)