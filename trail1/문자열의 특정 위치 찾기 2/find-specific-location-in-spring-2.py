words = ['apple', 'banana', 'grape', 'blueberry', 'orange']
char = input()
cnt = 0
ans = []
for word in words:
    if char == word[2] or char == word[3]:
        ans.append(word)
        cnt += 1

for i in ans:
    print(i)
print(cnt)