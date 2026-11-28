
def find_num(a):
    ans = ''
    for i in a:
        if i.isdigit():
            ans += i
        else:
            return int(ans)
    
    return int(ans)


a, b = input().split()

print(find_num(a) + find_num(b))