# https://www.hackerrank.com/challenges/re-sub-regex-substitution/problem

import re

def replaceable(match):
    text = match.group(0)
    if text == '&&':
        return 'and'
    elif text == '||':
        return 'or'

expression = re.compile(r'((?<= )(&&)(?= )|(?<= )(\|\|)(?= ))')

n = int(input())
for _ in range(n):
    s = input()
    print(re.sub(expression, replaceable, s))


#s = 'if a + b > 0 &&  || a - b < 0:'
#print(re.sub(expression, replaceable, s))


test = 'x  & &&| && ||  ||  |x'
print(re.sub(expression, replaceable, test))




