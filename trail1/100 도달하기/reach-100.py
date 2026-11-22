n = int(input())

ans = [1, n]

while ans[-1] < 100:
    ans.append(
        ans[len(ans)-1]
        + ans[len(ans)-2]
        )

print(' '.join(map(str,ans)))