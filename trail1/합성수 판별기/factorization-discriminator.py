def is_num(n):
    result = 'N'
    for i in range(2, n):
        if n % i == 0:
            result = 'C'
            break

    print(result)


n = int(input())
is_num(n)
