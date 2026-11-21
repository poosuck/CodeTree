def is_passed(scores):

    average = sum(scores) / len(scores)
    if average >= 60:
        print('pass')
        return 1

    else:
        print('fail')
        return 0


n = int(input())
cnt = 0
for i in range(n):
    scores = list(map(int, input().split()))

    cnt += is_passed(scores)

print(cnt)