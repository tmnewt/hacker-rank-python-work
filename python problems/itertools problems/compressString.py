# https://www.hackerrank.com/challenges/compress-the-string/problem

from itertools import groupby

s = '1222311'

for k, g in groupby(s):
    print(f'({len(list(g))}, {int(k)})', end=' ')    