def middle_값(A, B, C):
    print(
        int(
            B > A
            and B < C
        )
    )


A, B, C = map(int, input().split())
middle_값(A, B, C)