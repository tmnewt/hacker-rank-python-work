# https://www.hackerrank.com/challenges/py-collections-ordereddict/problem

from collections import OrderedDict

n = int(input())
purchases = OrderedDict()
for _ in range(n):
    line = input().split()
    k = ' '.join(line[:-1]);  p = int(line[-1])
    if k not in purchases:
        purchases[k] = p
    else:
        purchases[k] += p

for k, v in purchases.items():
    print(k, v)