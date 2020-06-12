# https://www.hackerrank.com/challenges/np-polynomials/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

import numpy as np

polys = np.array(list(map(float, input().split())))
x = int(input())

print(np.polyval(polys, x))

print(np.roots([1, -11, 9, 11, -10]))