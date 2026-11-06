def is_adult(성별, 나이):
    if int(나이) >= 19:
        if int(성별) == 0:
            print('MAN')
        else:
            print('WOMAN')
    
    else:
        if int(성별) == 0:
            print('BOY')
        else:
            print('GIRL')

성별, 나이 = [input() for _ in range(2)]
is_adult(성별, 나이)

