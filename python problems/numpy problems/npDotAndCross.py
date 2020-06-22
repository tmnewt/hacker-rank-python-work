# https://www.hackerrank.com/challenges/np-dot-and-cross/problem?h_r=internal-search

import numpy as np

n = int(input())

arr1 = np.array([list(map(int, input().split())) for _ in range(n)])
arr2 = np.array([list(map(int, input().split())) for _ in range(n)])

print(np.dot(arr1, arr2))