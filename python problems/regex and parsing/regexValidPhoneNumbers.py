# https://www.hackerrank.com/challenges/validating-the-phone-number/problem

import re

expr = re.compile(r'^([789]\d{9})$')
n = int(input())
for _ in range(n):
    try: 
        b = re.match(expr, input()).group(0)
        print('YES')
    except AttributeError:
        print('NO')






# test code:
#test = '4587456281'

#
#b = re.match(expr, test)
#try:
#    b.group(0)
#    print(True)
#except AttributeError:
#    print(False)