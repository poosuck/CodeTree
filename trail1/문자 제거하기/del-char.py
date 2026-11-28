string = list(input())

for _ in range(len(string) - 1):

    num = int(input())

    if num >= len(string):
        num = len(string) - 1


    string.pop(num)

    print(''.join(string))