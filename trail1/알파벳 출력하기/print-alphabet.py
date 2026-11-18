n = int(input())

num = 65

for i in range(1, n+1):
    for j in range(1, i+1):
        print(chr(num), end='')
        num += 1
        if num == 91:
            num = 65
    print()
