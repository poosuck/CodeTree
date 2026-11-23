person = [tuple(input().split()) for _ in range(3)]
A=B=C=D = 0

for 증상, temp in person:
    temp = int(temp)
    if (
        증상 == 'Y'
        and temp >= 37
    ):
        A += 1
    
    elif (
        증상 == 'N'
        and temp >= 37
    ):
        B += 1
    
    elif (
        증상 == 'Y'
        and temp < 37
    ):
        C += 1
    
    else:
        D += 1

if A >= 2:
    print(f'{A} {B} {C} {D} E')
else:
    print(f'{A} {B} {C} {D}')
