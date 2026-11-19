def is_jin(num):
    global cnt
    jins = []
    for i in range(1, num):
        if num % i == 0:
            jins.append(i)
    
    if sum(jins) == num:
        cnt += 1


start, end = map(int, input().split())
    
# Please write your code here.
cnt = 0

for num in range(start, end+1):
    is_jin(num)


print(cnt)