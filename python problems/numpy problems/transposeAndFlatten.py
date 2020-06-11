# https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem

# In this problem you will need to write your own input code for a 2 dimensional array of N x M elements.
# then simply transpose and then flatten the inputs

import numpy as np

def transposeAndFlatten(arr):
    return np.transpose(np.array(arr)).flatten()

nm = input().split()
n = int(nm[0])
m = int(nm[1])
a = []

for i in range(n):
    readIn = input().split()
    line = [ int(j) for j in readIn]
    a.append(line)

print(transposeAndFlatten(a))

