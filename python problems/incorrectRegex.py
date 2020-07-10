# https://www.hackerrank.com/challenges/incorrect-regex/problem?h_r=next-challenge&h_v=zen

# wish they had made this a bit more challenging...

import re

def checkRegex(s: str):
    try:
        a = re.compile(s)
        print(True)
    except re.error:
        print(False)
    
n = int(input())
for _ in range(n):
    checkRegex(input())
    