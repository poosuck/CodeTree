def score(num1, num2):
    if num1 >= 90:
        if num2 >= 95:
            print(100000)
        elif num2 >= 90:
            print(50000)
        else:
            print(0)
    else:
        print(0)



num1, num2 = map(int, input().split())

score(num1, num2)