A, B = map(int, input().split())

num = A
for i in range(A+1, B+1):
    num *= i

print(num)