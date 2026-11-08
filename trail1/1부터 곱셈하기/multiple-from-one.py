N = int(input())

ans = 1

for i in range(1, 11):
    ans *= i

    if ans >= N:
        print(i)
        break
