# https://www.hackerrank.com/challenges/itertools-combinations/problem

from itertools import combinations

s, k = input().split()
s = list(s)
s.sort()
k = int(k)
outs = []
for i in range(1, k+1):
    com = list(combinations(s,i))
    for j in com:
        outs.append(j)
for i in outs:
    print(''.join(i))

