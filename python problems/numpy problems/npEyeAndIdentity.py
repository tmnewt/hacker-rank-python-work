# https://www.hackerrank.com/challenges/np-eye-and-identity/problem

import numpy as np

n, m = map(int, input().split())
print(str(np.eye(n,m)).replace('1', ' 1').replace('0', ' 0'))

x, y = map(np.int, input().split())
print(np.eye(x, y))

# didn't know I could use k to offest the start of the diagonal...
#print(np.eye(8, 7, -2))