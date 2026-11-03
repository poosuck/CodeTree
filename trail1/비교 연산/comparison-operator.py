def Is_True(A, B):
    print(int(A >= B))
    print(int(A > B))
    print(int(A <= B))
    print(int(A < B))
    print(int(A == B))
    print(int(A != B))


A, B = map(int, input().split())
Is_True(A, B)