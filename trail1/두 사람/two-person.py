def abc(a_a, a_s, b_a, b_s):
    if int(a_a) > 19 and a_s == 'M':
        print(1)
    elif int(b_a) > 19 and b_s == 'M':
        print(1)
    else:
        print(0)

a_a, a_s = input().split()
b_a, b_s = input().split()

abc(a_a, a_s, b_a, b_s)


