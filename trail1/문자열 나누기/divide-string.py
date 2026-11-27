n = int(input())

ans = ''

a = list(input().split())

for i in a:
    ans += i


for i in range(len(ans)):
    if (i+1) % 5 == 0:
        print(ans[i], end='')
        print() 
    else:
        print(ans[i], end='')
        


