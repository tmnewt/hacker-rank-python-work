# https://www.hackerrank.com/challenges/np-zeros-and-ones/problem


# You are given the shape of the array in the form of space-separated integers, 
# each integer representing the size of different dimensions, 
# your task is to print an array of the given shape and integer type 
# using the tools numpy.zeros and numpy.ones.

# constraints:   1 <= each integer <= 3

# Output Format:
#       First, print the array using the numpy.zeros tool and then 
#       print the array with the numpy.ones tool. 

# also you will need to write your own reader.

import numpy as np
def zerosAndOnes(a, b, c):
    print(np.zeros((a, b, c), dtype= np.int))
    print(np.ones((a, b, c), dtype= np.int))

x, y, z = map(int, input().split())

zerosAndOnes(x, y, z)