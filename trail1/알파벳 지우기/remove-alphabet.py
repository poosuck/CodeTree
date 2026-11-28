def find_num(char):
    ans = ''
    for i in char:
        if i.isdigit():
            ans += i

    return int(ans)


a = input()
b = input()

print(find_num(a) + find_num(b))