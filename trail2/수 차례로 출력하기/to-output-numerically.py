def plus(n):
    n += 1
    print(n, end=' ')


def minus(n):
    n -= 1
    print(n, end=' ')


def number(num):

    while num < n:
        plus(num)
        num += 1

    print()
    num += 1

    while num > 1:
        minus(num)
        num -= 1



n = int(input())

# Please write your code here.


num = 0
number(0)