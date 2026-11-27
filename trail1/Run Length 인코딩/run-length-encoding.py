A = input()

# 출력할 빈 문자열 생성
char_lst = ''
cnt = 1
# Please write your code here.

# 문자열 순회
# 현재 문자 저장, 나온 횟수 카운트
# 문자가 바뀌면 문자와 카운트 저장
# 리스트 자르기, 문자, 카운트 초기화

for i in range(len(A)-1):
    now = i
    if A[i] == A[i+1]:
        cnt += 1
    else:
        char_lst += A[i]
        char_lst += str(cnt)
        cnt = 1

char_lst += A[-1]
char_lst += str(cnt)

print(len(char_lst))
print(char_lst)