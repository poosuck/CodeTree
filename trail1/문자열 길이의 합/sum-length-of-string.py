n = int(input())

char_cnt = 0
total_len = 0

for _ in range(n):
    # 단어 입력 받아서 첫번째 글자가 a면 카운트 1 증가
    # 단어 길이 누적
    word = input()
    if word[0] == 'a':
        char_cnt += 1
    
    total_len += len(word)

print(total_len, char_cnt)