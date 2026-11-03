def 최솟갑과일치하냐(a, b, c):
    print(int(a == min(a, b, c)), end=' ')
    print(int(a == b == c))


a, b, c = map(int, input().split())
최솟갑과일치하냐(a, b, c)
