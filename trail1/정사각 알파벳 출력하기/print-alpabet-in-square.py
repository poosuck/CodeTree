n = int(input())
num = 65

for i in range(n):
    for j in range(n):
        if j == n-1:
            print(chr(num), end='')
            num += 1
            print()
        else:
            print(chr(num), end='')
            num += 1