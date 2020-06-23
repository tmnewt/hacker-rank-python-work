# https://www.hackerrank.com/challenges/python-string-formatting/problem

def print_formatted(number):
    space = len(f'{number:b}')
    for i in range(1, number+1):
        print(f'{i:{space}d} {i:{space}o} {i:{space}X} {i:{space}b}')

print_formatted(17)