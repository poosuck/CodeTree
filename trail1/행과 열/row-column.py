a, b = map(int, input().split())

for row in range(1, a+1):
    num = row
    for col in range(b):
        
        print(row, end=' ')
        row += num
    print()