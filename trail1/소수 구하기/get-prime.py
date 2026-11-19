def is_sosu(num):
    cnt = 0
    for i in range(1, num+1):
        if num % i == 0:
            cnt += 1
    
    if cnt == 2:
        ans.append(num)
    


n = int(input())
ans = []

for i in range(1, n+1):
    is_sosu(i)

for i in ans:
    print(i, end=' ')