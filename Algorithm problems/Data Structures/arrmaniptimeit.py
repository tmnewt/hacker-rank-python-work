# https://www.hackerrank.com/challenges/crush/problem

import os
import time

start = time.time()

def arrayManipulation_Sum_Prefix(n: int, queries: list):
    arr = [0 for _ in range(n+1)]
    for query in queries:
        a = query[0]-1
        b = query[1]
        k = query[2]
        arr[a] += k
        arr[b] -= k
        #print(arr)
    
    answer = prefixSum(arr)
    return answer

def prefixSum(arr):
    running_sum = 0
    i = 0
    end = len(arr)
    while i < end:
        arr[i] = running_sum + arr[i]
        running_sum = arr[i]
        #print(arr)
        i+=1
    
    return max(arr)

os.chdir('Algorithm problems\\Data Structures')
fp = open('arraymaniptest9.txt', 'r')
lines = fp.readlines()
fp.close

startline = lines[0].rstrip().split()
size = int(startline[0])
runs = int(startline[1])

test_queries = []

for s_itr in range(runs):
    test_queries.append(list(map(int, lines[s_itr+1].rstrip().split())))

print(arrayManipulation_Sum_Prefix(size, test_queries))

end = time.time()
print(end-start)