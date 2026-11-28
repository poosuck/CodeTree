char1, char2 = map(ord, input().split())

print(char1+char2, max(char1, char2) - min(char1, char2))