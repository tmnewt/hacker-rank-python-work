# https://www.hackerrank.com/challenges/np-shape-reshape/problem

import numpy as np

test = [1,2,3,4,5,6,7,8,9]

myArr = np.array(list(map(int, input().split())))
print(np.reshape(myArr, (3,3)))