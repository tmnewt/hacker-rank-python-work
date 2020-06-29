# https://www.hackerrank.com/challenges/defaultdict-tutorial/problem

from collections import defaultdict

n, m = list(map(int, input().split()))
words = defaultdict(list)
inns = []

for i in range(n):
    words[input()].append(str(i+1))

for j in range(m):
    ElmIndexes = words[input()]
    if len(ElmIndexes) != 0:
        inns.append(ElmIndexes)
    else:
        inns.append([str(-1)])

for y in inns:
    print(' '.join(list(y)))

# some example code;

#d = defaultdict(list)
#d['python'].append('awesome')
#d['something-else'].append('not relevent')
#d['python'].append('language')
#for i in d.items():
#    print(i)
#
#print(d.get('python'))
## equivalent to
#print(d['python'])