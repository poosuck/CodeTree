a = 'ee'
b = 'ab'

a_ans = 'No'
b_ans = 'No'

A = input()

for i in range(len(A)-1):
    if A[i:i+2] == a:
        a_ans = 'Yes'
    elif A[i:i+2] == b:
        b_ans = 'Yes'

print(a_ans, b_ans)