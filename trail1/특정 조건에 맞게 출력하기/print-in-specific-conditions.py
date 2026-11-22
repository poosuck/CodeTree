lst = list(map(int, input().split()))

ans = []

for i in range(len(lst)):
    if lst[i] == 0:
        for j in range(i):
            if lst[j] % 2 == 1:
                ans.append(lst[j] + 3)
            else:
                ans.append(lst[j] // 2)
        break


print(' '.join(map(str,ans)))