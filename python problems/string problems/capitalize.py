# https://www.hackerrank.com/challenges/capitalize/problem?h_r=next-challenge&h_v=zen

def capitalizeFirstAndLast(s: str):
    return ' '.join(list(map(str.capitalize, s.split(' '))))
    

print(capitalizeFirstAndLast('1 2 2 3 4 5 6 7 8  9'))
print(capitalizeFirstAndLast('this is a test  2 bee   completed'))
