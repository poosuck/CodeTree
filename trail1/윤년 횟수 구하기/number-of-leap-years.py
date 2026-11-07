def is_yun(year):
    global cnt

    if (
        year % 4 != 0
        or (year % 100 == 0 and year % 400 != 0)
    ):
        cnt += 0
    
    else:
        cnt += 1


year = int(input())
cnt = 0
for i in range(1, year + 1):
    is_yun(i)


print(cnt)