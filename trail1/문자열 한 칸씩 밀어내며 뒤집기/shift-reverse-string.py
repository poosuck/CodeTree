def order(chars, num):
    
    if num == 1:
       chars = chars[1:] + chars[0]
       return chars

    elif num == 2:
        chars = chars[-1] + chars[:len(chars)-1]
        return chars
    
    else:
        chars = chars[::-1]
        return chars


chars, q = input().split()
q = int(q)
queries = [int(input()) for _ in range(q)]

# Please write your code here.
for i in queries:
    chars = order(chars, i)
    print(chars)
