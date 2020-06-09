# https://www.hackerrank.com/challenges/closest-numbers/problem?h_r=next-challenge&h_v=zen

import os
import numpy as np

def closestNumbers(arr):
    arr.sort()
    diff = abs(max(arr)-min(arr))
    for i in range(len(arr)-1):
        if abs(arr[i+1]-arr[i]) < diff:
            diff = arr[i+1] - arr[i]
    outs = []
    for i in range(len(arr)-1):
        if abs(arr[i+1]-arr[i]) == diff:
            outs.append(arr[i])
            outs.append(arr[i+1])
    return outs



os.chdir('Algorithm problems\\Sorting\\tests')
fp = open('large_random_ints_unique', 'r')
arr = list(map(int, fp.read().rstrip().split()))



#print('generating random list of unique integers from a uniform distribution')
#arr= list(np.random.choice(range(-10000000, 10000000), 20000))

outs = closestNumbers(arr)

print(f'size of inputs was a length of {len(arr)}')
print(f'smallest value from input is {min(arr)}')
print(f'largest value from input is {max(arr)}')
print(f'maximum difference is {abs(max(arr)-min(arr))}')
print(f'smallest difference is {abs(outs[1]-outs[0])}')
print(f'number of pairs of smallest difference is {len(outs)}')

arr_actual = np.array(arr)
print(np.mean(arr_actual))
print(np.median(arr_actual))
print(np.std(arr_actual))
