n = int(input())
nums = []
for i in range(n):
    a = int(input())
    nums.append(a)



for num in nums:
    cnt = 0
    while True:
        if num == 1:
            break
        elif num % 2 == 0:
            num //= 2
            cnt += 1
            if num == 1:
                break
        else:
            num = num * 3 + 1
            cnt += 1
            if num == 1:
                break

    print(cnt)
    
