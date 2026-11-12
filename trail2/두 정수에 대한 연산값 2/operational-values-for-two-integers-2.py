def num(num1, num2):
    if num1 > num2:
        num2 += 10
        num1 *= 2
    else:
        num1 += 10
        num2 *= 2

    return num1, num2


a, b = map(int, input().split())
a, b = num(a, b)
print(a, b)