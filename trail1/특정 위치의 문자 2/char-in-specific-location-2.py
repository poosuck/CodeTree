lst = list(input().split())

for idx in range(len(lst)):
    if (
        idx == 1
        or idx == 4
        or idx == 7
    ):
        print(lst[idx], end=' ')