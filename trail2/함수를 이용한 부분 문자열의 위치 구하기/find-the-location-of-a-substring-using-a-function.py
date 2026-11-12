def idx_char(text, pattern):
    found = 0
    # 문자열 순회
    for i in range(len(text)):
        compare = text[i:i+len(pattern)]
        if compare == pattern:
            print(i)
            found = 1
            break

    if found == 0:
        print(-1)
        return

text = input()
pattern = input()

# Please write your code here.

idx_char(text, pattern)