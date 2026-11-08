students = {
    'John' : 1,
    'Tom' : 2,
    'Paul' : 3,
    'Sam' : 4,
}

while True:
    try:
        num = int(input())

    except EOFError:
        break


    for key, value in students.items():
        if num == value:
            print(key)
            break
    else:
        print('Vacancy')
        break