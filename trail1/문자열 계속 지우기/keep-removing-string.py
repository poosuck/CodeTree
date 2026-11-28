def erase(A, B):
    
    for i in range(len(A) - len(B) + 1):

        if A[i:i+len(B)] == B[:]:
            for j in range(i+len(B)-1, i-1, -1):
                A.pop(j)

            erase(A, B)

    return ''.join(A)


A = list(input())
B = list(input())

# Please write your code here.
print(erase(A, B))