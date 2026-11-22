lst = list(map(int, input().split())) + [0] *8

for i in range(2, len(lst)):
    lst[i] = (lst[i-1] + lst[i-2]) % 10

print(*lst)