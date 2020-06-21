# https://www.hackerrank.com/challenges/sherlock-and-squares/problem?h_r=internal-search

import math

# find number of squares inclusive in range.
# for example, how many perfect squares are there in the range a to b


# don't do precomputation attack...

# 3000 to 5000
# 60 , 70 
# a^(1/2) = 54.7, 
# b^(1/2) = 70.7
# [55.... 70]

def squares(a, b):
    low = math.ceil(a**(1/2))
    print(low)
    upp = math.floor(b**(1/2))
    print(upp)
    return (upp-low)+1

print(squares(3000, 5000), '\n')

print(squares(3,9), '\n')
print(squares(17,24))
