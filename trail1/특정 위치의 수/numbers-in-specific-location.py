arr = [0] + list(map(int, input().split()))

total = 0
for i in range(11):
    if (
        i == 3
        or i == 5
        or i == 10
    ):
        total += arr[i]

print(total)