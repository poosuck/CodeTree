def q1(word, a, b):
    a, b = int(a), int(b)

    a -= 1
    b -= 1

    target_a = word[a]
    target_b = word[b]

    word[a] = target_b
    word[b] = target_a
    
    print(''.join(word))


def q2(word, a, b):
    for i in range(len(word)):
        if word[i] == a:
            word[i] = b
    
    print(''.join(word))


word, n = input().split()
word = list(word)
n = int(n)

questions = []
for _ in range(n):
    q, a, b = input().split()
    questions.append((q,a,b))


for q, a, b in questions:
    if q == '1':
        q1(word, a, b)
    else:
        q2(word, a, b)