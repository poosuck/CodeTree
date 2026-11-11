def say_hello(cnt):

    if cnt == n:
        return
    
    print('HelloWorld')
    cnt += 1
    say_hello(cnt)

    
n = int(input())

# Please write your code here.
cnt = 0
say_hello(cnt)