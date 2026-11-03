def 계산(a, b):
    print(int(a >= b))
    print(int(a > b))
    print(int(b >= a))
    print(int(b > a))


a, b = map(int, input().split())
계산(a, b)