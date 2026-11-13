A = input()

cnt = 0

for i in range(len(A)):
    if A[i] == '(':
        for j in A[i:]:
            if j == ')':
                cnt += 1

print(cnt)