'''
a = 1, b = 2 일때
print(a < b) -> True
int(True) -> 1
print(int(a < b)) -> True
'''
def Is_True(A, B):
    print(int(A >= B))
    print(int(A > B))
    print(int(A <= B))
    print(int(A < B))
    print(int(A == B))
    print(int(A != B))


A, B = map(int, input().split())
Is_True(A, B)