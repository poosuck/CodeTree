def question_1(alp):
    print(Ns[alp-1])


def question_2(alp):
    if alp in Ns:
        print(Ns.index(alp)+1)
    else:
        print(0)
    
def question_3(alp1, alp2):
    for i in range(alp1-1, alp2):
        print(Ns[i], end=' ')
    print()


N, Q = map(int, input().split())
Ns = list(map(int, input().split()))

commands = [tuple(map(int, input().split())) for _ in range(Q)]



for command in commands:
    if command[0] == 1:
        question_1(command[1])
    elif command[0] == 2:
        question_2(command[1])
    else:
        question_3(command[1], command[2])


# print(N, Q)
# print(Ns)
# print(commands)