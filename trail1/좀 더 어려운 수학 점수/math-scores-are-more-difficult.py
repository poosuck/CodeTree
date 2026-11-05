def high(a_math, a_eng, b_math, b_eng):
    if a_math > b_math:
        print('A')
    elif a_math < b_math:
        print('B')
    elif a_math == b_math:
        if a_eng > b_eng:
            print('A')
        else:
            print('B')



a_math, a_eng = map(int, input().split())
b_math, b_eng = map(int, input().split())
high(a_math, a_eng, b_math, b_eng)