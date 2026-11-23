a, b = map(int, input().split())
A = list(input().split())
B = list(input().split())

for i in range(len(A) - len(B)+1):
    lst_a = A[i:i+len(B)]
    if lst_a == B:
        print('Yes')
        break
else:
    print('No')