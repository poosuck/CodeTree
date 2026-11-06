def is_yun(year):
    if (
        year % 4 != 0
        or (year % 100 == 0
        and year % 400 != 0)
    ):
        print('false')
    else:
        print('true')


year = int(input())
is_yun(year)