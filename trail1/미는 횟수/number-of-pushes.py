a = input()
b = input()

cnt = 0

while True:
    if cnt == len(a):
        print(-1)
        break

    if a == b:
        print(cnt)
        break

    else:
        cnt += 1
        a = a[-1] + a[:len(a)-1]