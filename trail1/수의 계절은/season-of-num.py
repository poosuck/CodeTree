def when(M):
    if 3 <= M <= 5:
        print('Spring')
    if 6 <= M <= 8:
        print('Summer')
    if 9 <= M <= 11:
        print('Fall')
    if M == 12 or 1 <= M <= 2:
        print('Winter')


M = int(input())

when(M)