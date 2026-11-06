A, B = map(int, input().split())
num = A-1
while A-1 <= num <= B:
    num += 1
    if num % 2 == 0:
        print(num, end=' ')
