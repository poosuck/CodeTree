def print_char(char):
    if char == 'S':
        print('Superior')
    elif char == 'A':
        print('Excellent')
    elif char == 'B':
        print('Good')
    elif char == 'C':
        print('Usually')
    elif char == 'D':
        print('Effort')
    else:
        print('Failure')


char = input()
print_char(char)