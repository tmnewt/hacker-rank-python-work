# https://www.hackerrank.com/challenges/iterables-and-iterators/problem

from itertools import combinations, groupby

n = int(input())
s = input().split()
k = int(input())

com = list(combinations(s, k))
combs = 0
for i in com:
    if 'a' in i:
        combs += 1

print(f'{combs/len(com):1f}')

