# https://www.hackerrank.com/challenges/itertools-permutations/problem

from itertools import permutations
s, n = input().split()
n = int(n)
outs = list(permutations(s, n))
outs.sort()
for i in outs:
    print(''.join(list(i)))