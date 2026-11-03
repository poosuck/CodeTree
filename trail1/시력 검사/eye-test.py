def good_eye_deer(left, right):
    if (left and right) >= 1.0:
        print('High')

    elif (left and right) >= 0.5:
        print('Middle')
        
    else:
        print('Low')
    

left, right = (float(input()) for _ in range(2))

good_eye_deer(left, right)