n = int(input())

lst = list(map(int, input().split()))

cnt_2 = 0

for i in range(len(lst)):
    if lst[i] == 2:
        cnt_2 += 1
        if cnt_2 == 3:
            print(i+1)