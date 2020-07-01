# https://www.hackerrank.com/challenges/re-findall-re-finditer/problem

import re

s = re.findall(r'[^aeiouAEIOU0-9]([aeiouAEIOU]{2,})(?=[^aeiouAEIOU0-9])', input())
for i in s:
    print(i)