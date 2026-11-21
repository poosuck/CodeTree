def is_num(lst):
    total = 0
    cnt = 0
    for num in lst:
        if num != 0:
            if num % 2 == 0:
                cnt += 1
                total += num
        else:
            break
    
    print(cnt, total)


lst = list(map(int, input().split()))

is_num(lst)
