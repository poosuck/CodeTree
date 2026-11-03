def print_a(a):
    if a % 2 == 0:
        a //= 2
    if a % 2 == 1:
        a = (a + 1) // 2
    print(a)


a = int(input())
print_a(a)