def is35(a):
    print(
        int(
            a % 3 == 0
            or a % 5 == 0
        )
    )


a = int(input())
is35(a)