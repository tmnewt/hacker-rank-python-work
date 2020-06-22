# https://www.hackerrank.com/challenges/np-sum-and-prod/problem

import numpy as np

n, m = map(int, input().split())

arr = np.array([list(map(int, input().split())) for _ in range(n)])

sum_arr = np.sum(arr, axis=0)
print(np.prod(sum_arr))

