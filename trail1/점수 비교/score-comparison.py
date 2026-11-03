def compare(A_math, A_english, B_math, B_english):
    print(
        int(
            A_math > B_math
        and A_english > B_english
        )
    )



A_math, A_english = map(int, input().split())
B_math, B_english = map(int, input().split())

compare(A_math, A_english, B_math, B_english)