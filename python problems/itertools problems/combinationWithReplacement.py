# https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem

from itertools import combinations_with_replacement #combinations

#print(list(combinations('HACK', 2)))
#print(list(combinations_with_replacement('HACK',2)))

s, k = input().split()
s = list(s)
s.sort()
k = int(k)
for i in list(combinations_with_replacement(s, k)):
    print(''.join(i))
