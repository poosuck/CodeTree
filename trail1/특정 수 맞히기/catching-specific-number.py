while True:
    score = int(input())

    if score == 25:
        print('Good')
        break
    elif score > 25:
        print('Lower')
    else:
        print('Higher')