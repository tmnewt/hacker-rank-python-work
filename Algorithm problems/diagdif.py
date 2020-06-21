# https://www.hackerrank.com/challenges/diagonal-difference/problem?h_r=internal-search

test_array1 = [
[11,2,4],
[4,5,6],
[10,8,-12]
]

test_array2 = [
    [0, 1, 2, 3],
    [9, 4, 2, 7],
    [7, 8, 0, 4],
    [4, 5, 6, 7]
]


def diagonalDifference(arr):
    # Write your code here
    d1 = 0
    d2 = 0
    for i, j in zip(range(len(arr)), range(len(arr)-1,-1,-1)):
        d1 += arr[i][i]
        # sum for diagonal 2:
        d2 += arr[i][j]
    return abs(d1-d2)

print(diagonalDifference(test_array1))
print(diagonalDifference(test_array2))

