n = int(input())

words = [input() for _ in range(n)]

char = input()
cnt = 0
length = 0
for word in words:
    if word[0] == char:
        cnt += 1
        length += len(word)

print(f'{cnt} {length/cnt:.2f}')