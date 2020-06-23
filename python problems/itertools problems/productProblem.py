# https://www.hackerrank.com/challenges/itertools-product/problem
from itertools import product
A = [list(map(int, input().split())), list(map(int, input().split()))]
print(' '.join(list(map(str, list(product(*A))))))
