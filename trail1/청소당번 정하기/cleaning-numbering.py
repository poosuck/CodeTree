num = int(input())

cnt2 = 0
cnt3 = 0
cnt12 = 0

for i in range(num, 0, -1):
    if i % 12 == 0:
        cnt12 += 1

    elif i % 3 == 0:
        cnt3 += 1

    elif i % 2 == 0:
        cnt2 += 1
    else:
        continue


print(cnt2, cnt3, cnt12)