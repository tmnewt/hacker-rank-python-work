# https://www.hackerrank.com/challenges/introduction-to-regex/problem

import re

expr = re.compile(r'^[+-]?\d{0,}\.\d{1,}$')
for _ in range(int(input())):
    if re.match(expr, input()) == None:
        print(False)
    else:
        print(True)

