def num(A, B):
    number = A
    print(number, end=' ')
    while number <= B:
        if number % 2 == 1:
            number *= 2
        elif number % 2 == 0:
            number += 3
        if number <= B:
            print(number, end=' ')


A, B = map(int, input().split())
num(A, B)
