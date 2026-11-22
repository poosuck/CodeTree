lst = list(map(int, input().split()))

total1 = 0
total2 = 0
cnt = 0

for i in range(len(lst)):
    if i % 2 == 1:
        total1 += lst[i]

for i in range(2, len(lst), 3):
    cnt += 1
    total2 += lst[i]

average = total2 / cnt

print(f'{total1} {average:.1f}')