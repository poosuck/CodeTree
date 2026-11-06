A, B = map(int, input().split())
num = A
while num <= B:
    if num % 2 == 0:
        print(num, end=' ')
    num += 1
