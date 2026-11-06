B, A = map(int, input().split())
num = B
while num >= A:
    if num % 2 == 0:
        print(num, end=' ')
    num -= 1