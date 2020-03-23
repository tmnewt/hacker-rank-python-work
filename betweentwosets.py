# test case
#       a = [2,   6]
#       b = [24, 36]
#
# Output: (at least I think this the expected output) 
#           2

#######################################################

# another test case
#       a = [2, 4]
#       b = [16, 32, 96]
#
# Output:
#           3

# explanation:
# 2 and 4 divide evenly into 4, 8, 12, and 16.
# 4, 8, and 16 divide evenly into 16, 32, 96.
# 4, 8, and 16 are the only three numbers for which each
# element of a is a factor and each is a factor all
# elements of b.

# So,
# given two arrays of integers determine all integers
# that satisfy the following two conditions:
#   1. The elements of the first array are all factors of the integer being considered
#   2. The integer being considered is a factor of all elements of the second array

# only need to count up to 100 I think...
# still, I should try to speed it up.

def getTotalX(a, b):
    tmp = []
    tmp.append(min(a))
    tmp.append(min(b))
    num = max(tmp)
    
   
    #print(num)
    #for i in range(num+1):
    #    pass

a = [2, 4]
b = [16, 32, 96]

getTotalX(a,b)