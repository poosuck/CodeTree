a = input()

ans = ''

for i in a:
    if i.isalpha():
        ans += i.upper()

print(ans)