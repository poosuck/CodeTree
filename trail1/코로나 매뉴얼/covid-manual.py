def is_emergency(lst):
    cnt = 0
    for is_감기, temp in lst:
        if is_감기 == 'Y' and int(temp) >= 37:
            cnt += 1
    
    if cnt >= 2:
        print('E')
    else:
        print('N')


lst = []
for _ in range(3):
    lst.append(input().split())


is_emergency(lst)