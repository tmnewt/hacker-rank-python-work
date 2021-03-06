# https://www.hackerrank.com/challenges/max-array-sum/problem

# Given an array of integers, find the subset of non-adjacent elements with the maximum sum.
# For example:
#   arr = [-2, 1, 3, -4, 5, 6] has the maximum subset sum of 9.

# The trick here is keep track of the maximum sum value for each element in the array, 
#  using a 'shadow' array while following these rules:
#       
#   The maximum value for the next element in the original array is defined as,  
#
#   1. The maximum is the sum of the maximum value from 2 elements prior + the current value,
#       Or,
#   2. The current element itself.
#       Or,
#   3. The maximum is from an earlier index.
#
#
# Using the array example above, we get the following
#       Array                         Maximum "shadow" array     Max Value           Comments
#   [ '-2'  1  3  -4  5  6 ]             [ -2 ]                    -2             First 2 indexes get special treatment.  
#   [  -2  '1' 3  -4  5  6 ]             [ -2  1]                   1             1 replaces -2 as current max
#   [  -2   1 '3' -4  5  6 ]             [ -2  1  3]                3             3 replaces  1 as current max  (cant be 1 + 3 = 4 because 1 and 3 elements are next to each other)
#   [  -2   1  3 '-4' 5  6 ]             [ -2  1  3  3 ]            3             3 remains as max 
#   [  -2   1  3  -4 '5' 6 ]             [ -2  1  3  3  8 ]      3 + 5 = 8        8 becomes the new max.
#   [  -2   1  3  -4  5 '6']             [ -2  1  3  3  8  9]    3 + 6 = 9        9 becomes the new max.
#   Done
#
#   Wait, what happened there at the end? How did the program know to use the 3 from earlier? Answer, that 3 is NOT from the original
#       array, it is actually from the 3 in the "shadow" array. Remember rule 1 from above. By checking the "shadow" maximum value of the
#       element 2 spots before the current value, we can test if adding it to the current value will produce a new maximum.
# 
# 
# Now, it should be possible to not even need to build a parallel list of maximum values. All it requires is 2 variables. But I'm
#   to lazy to think through that 
# 

def maxSubsetSum(arr):
    shadow_max = []
    shadow_max.append(arr[0])
    if arr[1] > arr[0]:
        shadow_max.append(arr[1])
        #maximum = arr[1];  second = arr[0]
    else:
        shadow_max.append(arr[0])
        #maximum = arr[0];  second = arr[1]
    arr = arr[2:]
    for elem in arr:
        last_max = shadow_max[-1]
        elem_sum = elem + shadow_max[-2]
        this_max = max(elem_sum, elem, last_max)
        shadow_max.append(this_max)

    return shadow_max[-1]

print(maxSubsetSum([3, 7, 4, 6, 5]))