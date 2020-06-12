# https://www.hackerrank.com/challenges/np-min-and-max/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

# use numpy min method on axis 1 and then find the max of that result.

import numpy as np

n, m = map(int, input().split())

arr = np.array([list(map(int, input().split())) for _ in range(n)])

print(np.max(np.min(arr, axis=1)))