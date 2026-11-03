def is_even(num):
    if num % 2 == 0:
        print('even')
    else:
        print('odd')


a, b = map(int, input().split())

is_even(a)
is_even(b)