# https://www.hackerrank.com/challenges/np-inner-and-outer/problem?h_r=internal-search

import numpy as np

a = np.array(list(map(int, input().split())))
b = np.array(list(map(int, input().split())))

print(np.inner(a, b))
print(np.outer(a, b))