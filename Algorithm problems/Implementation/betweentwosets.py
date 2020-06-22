# https://www.hackerrank.com/challenges/between-two-sets/problem?isFullScreen=false

#given tow arrays of ints determine all ints that satisfy the following conditions:
# 1. The elements of the FIRST array are all factors of the integer being considered
# 2. The integer being considered is a factor of all elements of the second array.

# so, given 2 arrays by incrementing am int value, i, we are  concerned with finding the following:
#
#       [2, 6]  all elements are factors of i  and i is a factor of all elements [24, 36]
#
#  we count up the instances of i.
# 
# For instance,
#       
#       [2, 6]  NOT all elements are factors of 5 and 5 is NOT a factor of all [24, 36]
#       [2, 6]  all elements are factors of 6 and 6 is a factor of all [24, 36]        <<< count this!
#       [2, 6]  NOT all elements are factors of 7 and 7 is NOT factor of all [24, 36]
#       ...
#       [2, 6]  all elements are factors of 12 and 12 is a factor of all [24, 36]        <<< count this!
# 
# There are no instances of i that satisfy the condition
# Task wants the count of i instances that worked. In the above case, return 2 (that's 2 counts of occurrences)
# 
# Some things to keep in mind to speed up this task:
# only need to get the factors of the lowest value in the 2nd array?
#
# another example; given [2, 4] and [16, 32, 96]
#                  return 3
#
# Guiding myself through step by step.
#   starting point:
#       Take all numbers below the smallest value in the 2nd array.
#       Find all numbers that can be cleanly divided by all elements in 1st array
#       
#              
#
#       if a[elm]%i == 0:
#            
#   


test_list1 = [2,4]
test_list2 = [16, 32, 96]

def getTotalX(a_list: list, b_list: list):
    # find lowest in b
    b_min = min(b_list)
    factors = []
    for i in range(1, b_min+1):
        if all([i%a==0 for a in a_list]):
            factors.append(i)
    #print(factors)
    
    #betweens = []
    count = 0
    for factor in factors:
        #print(f'Factors include: {factors}')
        #print(f'Testing factor: {factor}')
        if all([b%factor==0 for b in b_list]):
            count += 1
            #betweens.append(factor)
    return count



print(getTotalX(test_list1, test_list2))
