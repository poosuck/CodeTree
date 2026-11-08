N = int(input())
ans = 0
i = 1

while i <= 100:
    ans += i

    if ans < N:
        i += 1
    
    else:
        print(i)
        break