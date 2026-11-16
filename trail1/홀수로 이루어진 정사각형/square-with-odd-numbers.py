n = int(input())

for row in range(n):
    num = 11 + (2 * row)
    for col in range(n):
        print(num, end=' ')
        num += 2
    print()

