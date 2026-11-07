def is_369(N):
    if int(N) % 3 == 0:
        print(0, end=' ')
    elif '3' in N or '6' in N or '9' in N:
        print(0, end=' ')
    else:
        print(N, end=' ')


N = input()
for i in range(1, int(N) + 1):
    is_369(str(i))    