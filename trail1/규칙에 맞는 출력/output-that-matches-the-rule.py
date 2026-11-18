n = int(input())

for i in range(n):
    for j in range(abs(i-n), n+1):
        print(j, end=' ')
    print()
