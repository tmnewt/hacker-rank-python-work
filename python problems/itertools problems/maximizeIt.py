# https://www.hackerrank.com/challenges/maximize-it/problem?h_r=next-challenge&h_v=zen

# this is an optimization problem

from itertools import product

# example input
#m = 1000
#lines = [[5, 4], [7,8,9], [5,7,8,9,10]]


k, m = list(map(int, input().split()))
lines = []
for _ in range(k):
    line = list(map(int, input().split()))[1:]
    lines.append(line)
    # this can converted into list comprehension.

cartesianProduct = list(product(*lines))
results = []
for i in cartesianProduct:
    total = 0
    for j in i:
        total += j**2
    results.append(total%m)

print(max(results))
