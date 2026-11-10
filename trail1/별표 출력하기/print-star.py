n = int(input())

num = 1

while True:
    if n == 1:
        print('*')
        break
    else:
        print('* ' * num)
        if num < n:
            num += 1
        
        if num == n:
            for i in range(n, 0, -1):
                print('* ' * i)
            
            break
