def Is_True(A, B):
    if A >= B:
        print(1)
    else:
        print(0)

    if A > B:
        print(1)
    else:
        print(0)

    if B >= A:
        print(1)
    else:
        print(0)
    
    if B > A:
        print(1)
    else:
        print(0)

    if A == B:
        print(1)
    else:
        print(0)

    if A != B:
        print(1)
    else:
        print(0)


A, B = map(int, input().split())
Is_True(A, B)