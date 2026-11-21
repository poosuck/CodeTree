n = int(input())

lst = list(map(int, input().split()))

for i in lst[:]:
    if i % 2 != 0:
        lst.remove(i)

for i in range(len(lst)-1, -1, -1):
    print(lst[i], end=' ')
