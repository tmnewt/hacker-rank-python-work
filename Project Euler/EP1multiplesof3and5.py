# https://www.hackerrank.com/contests/projecteuler/challenges/euler001/problem

# Print an integer that denotes the sum of all the multiples of 3 OR 5 below N

import math

# the following works up to a point. Then floats starts causing problems.
def multiplesSumUnderN(n, k):
    n=n-1
    return int((k/2)*(math.floor(n/k))*(math.floor(n/k)+1))

def multiplesSum3And5(n): # under N
    return multiplesSumUnderN(n, 3) + multiplesSumUnderN(n, 5) - multiplesSumUnderN(n, 15)

print(multiplesSum3And5(10000000000000000000000))


# the following is the complete solution.

def multiplesSumUnderNAlt(n, k):
    n = n-1
    ground = n//k
    return k*((ground * (ground+1))//2)

#print(multiplesSumUnderNAlt(14, 3))

def multiplesSum3And5Alt(n):
    return multiplesSumUnderNAlt(n, 3) + multiplesSumUnderNAlt(n, 5) - multiplesSumUnderNAlt(n, 15)

print(multiplesSum3And5Alt(10000000000000000000000))