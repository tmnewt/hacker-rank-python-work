# https://www.hackerrank.com/challenges/2d-array/problem

# hour glass problem
# return the largest hourglass.

# given a 6 by 6 array there will always be 16 hourglasses
# hourglass starts at any index at or below 3 for both dimensions

# every hourglass is built in the format:
#           
#               n n n
#                 n
#               n n n
#
# 


def hourglassSum(arr):
    glasses = []
    for i in range(4):
        for j in range(4):
            glasses.append(arr[i][j] + arr[i][j+1]   + arr[i][j+2]
                              + arr[i+1][j+1] +
                    arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2])
    
    return max(glasses)


# works