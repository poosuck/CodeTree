ee_cnt = 0
eb_cnt = 0

a = input()
for i in range(len(a)-1):
    if a[i:i+2] == 'ee':
        ee_cnt += 1
    elif a[i:i+2] == 'eb':
        eb_cnt += 1

print(ee_cnt, eb_cnt)