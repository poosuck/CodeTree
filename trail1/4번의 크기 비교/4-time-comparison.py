def compare(a, b, c, d, e):
    print(int(a > b))
    print(int(a > c))
    print(int(a > d))
    print(int(a > e))



a = int(input())
b, c, d, e = map(int, input().split())
compare(a, b, c, d, e)