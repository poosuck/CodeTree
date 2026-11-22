n = int(input())

num = 0
cnt = 0

while cnt < 2:
    num += n
    if num % 5 == 0:
        cnt += 1
    print(num, end=' ')
