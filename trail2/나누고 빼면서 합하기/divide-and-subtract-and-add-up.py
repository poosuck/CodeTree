def abc(m):
    ans = A[m-1]

    while m != 1:
        if m % 2 == 1:
            m -= 1
            ans += A[m-1]

        else:
            m //= 2
            ans += A[m-1]
    
    return ans


n, m = map(int, input().split())
A = list(map(int, input().split()))

# Please write your code here.


print(abc(m))