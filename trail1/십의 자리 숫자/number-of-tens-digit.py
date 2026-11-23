lst = list(map(int, input().split()))
ans = []

for i in range(len(lst)):
    if lst[i] != 0:
        ans.append(lst[i] // 10)
    else:
        break

for i in range(9):
    print(f'{i+1} - {ans.count(i+1)}')
