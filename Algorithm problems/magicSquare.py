# magic square is an n x n matrix of distinct positive
# int from 1 to n^2 where the sum of any row, column, or
# diagonal of length n is always equal to the same num.
# a.k.a : the magic constant
# 
# Given 3 x 3 matrix  of random ints between 1 and 9
# 
# Our goal is to convert a given matrix into a magical square
# Every conversion of some int a to b requires cost. The cost
# is the absolute value. 
# 
# for example:
#       5  3  4                     8  3  4
#       1  5  8     converts to     1  5  9
#       6  4  2                     6  7  2
# 
# The first square is not a magic square, the latter is.
# It took a total cost of 7 to convert it.
# 
# 5 in the upper left is changed to 8
# 8 is in the middle right is changed to 9
# 7 in the bottom middle is changed to 4
# 
# The cost of this conversion is |5-8| + |8-9| + |4-7| = 7
# 
# There are multiple magical constants to work towards given 
# a random square matrix
# 
# For instance in the above square the sum values before conversion is, 
#                  = 15                                = 15
#       5   3   4  = 12                    8   3   4   = 15
#       1   5   8  = 14      converts to   1   5   9   = 15
#       6   4   2  = 12                    6   7   2   = 15
#       =   =   =  =                       =   =   =   = 
#       12  12  14   12                    15  15  15    15
# 
#  
# consider:      
#                  = 13                                = 15
#       4   8   2  = 14                    4  <9>  2   = 15
#       4   5   7  = 16      converts to  <3>  5   7   = 15
#       6   1   6  = 13                   <8>  1   6   = 15
#       =   =   =  =                       =   =   =   =
#       14  14  15   15                    15  15  15    15
# 
#   the cost for conversion is: |9-8| + |3-4| + |8-6| = 4
#   
#   are there other conversions? Yes, but they are more costlier.
#   
#                  = 13                                = 15
#       4   8   2  = 14                    4  <9>  2   = 15
#       4   5   7  = 16     converts to   <3>  5   7   = 15
#       6   1   6  = 13                   <8>  1   6   = 15
#       =   =   =  =                       =   =   =   =
#       14  14  15   15                    15  15  15    15
# 
#   
#       
#  only magic constant are 15 for 3 x 3 so move any and all values to equal
#  15  
# 
# 
# #     