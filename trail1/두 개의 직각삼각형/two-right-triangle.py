def star(num, times):
    print(f'{"*" * num}{" " * times}{"*" * num}')


n = int(input())

total = 2*n

for i in range(n, 0, -1):
    star(i, total - 2*i)