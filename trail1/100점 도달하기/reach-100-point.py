def your_score(num):

    score = {
        'A' : 90,
        'B' : 80,
        'C' : 70,
        'D' : 60,
        'F' : 0
    }

    while num <= 100:
        for key, value in score.items():
            if num >= value:
                print(key, end=' ')
                break
        num += 1


num = int(input())
your_score(num)