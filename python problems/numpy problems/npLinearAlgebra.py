# https://www.hackerrank.com/challenges/np-linear-algebra/problem?h_r=internal-search

# read the challenge before running...
import numpy as np
np.set_printoptions(legacy='1.13')

n = int(input())

arr = np.array([list(map(float, input().split())) for _ in range(n)])

print(np.linalg.det(arr))

# try single line:
print(np.linalg.det(np.array([list(map(float, input().split())) for _ in range(int(input()))])))