cnt = 0
ans = []

while True:
    word = input()

    if word == '0':
        break
    else:
        cnt += 1
        if cnt % 2 == 1:
            ans.append(word)

print(cnt)
for i in ans:
    print(i)