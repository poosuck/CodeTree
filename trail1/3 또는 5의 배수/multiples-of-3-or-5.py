def Yes_or_No(num):
    if num % 3 == 0:
        print('YES')
    else:
        print('NO')
    
    if num % 5 == 0:
        print('YES')
    else:
        print('NO')


num = int(input())
Yes_or_No(num)