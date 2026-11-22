n = int(input())

lst = list(map(int, input().split()))

for i in range(len(lst)):
    lst[i] = lst[i]**2

print(*lst)