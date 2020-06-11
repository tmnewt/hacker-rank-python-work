# https://www.hackerrank.com/challenges/np-concatenate/problem?h_r=next-challenge&h_v=zen

# Another read in problem. This time go right for the kill and concate everything on the spot.

import numpy as np

nmp = input().split()
n = int(nmp[0])
m = int(nmp[1])
p = int(nmp[2])

a = []
for i in range(n+m):
    a.append([ int(j) for j in input().split()])

a = np.array(a)

print(np.concatenate(a))


# better code:
n, m, p = map(int,input().split())
arrA = np.array([input().split() for _ in range(n)],int)
arrB = np.array([input().split() for _ in range(m)],int)
print(np.concatenate((arrA, arrB), axis = 0))