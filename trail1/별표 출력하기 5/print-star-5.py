def print_star(num):
    for _ in range(num):
        print('*'*num, end=' ')
    print()


n = int(input())

for i in range(n, 0, -1):
    print_star(i)
