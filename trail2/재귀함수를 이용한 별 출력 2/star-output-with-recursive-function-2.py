def make_star(n):
    if n == 0:
        return

    print('* ' * n)
    make_star(n-1)
    print('* ' * n)



n = int(input())

# Please write your code here.

make_star(n)