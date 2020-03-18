import math

arr = [
[11,2,4],
[4,5,6],
[10,8,-12]
]

test_array = [
    [0, 1, 2, 3],
    [9, 4, 2, 7],
    [7, 8, 0, 4],
    [4, 5, 6, 7]
]

d1 = 0
d2 = 0


for i, j in zip(range(len(arr)), range(len(arr)-1,-1,-1)):
    d1 += arr[i][i]
    # sum for diagonal 2:
    d2 += arr[i][j]

print(d1)
print(d2)

print(abs(d1-d2))

#for i, j in zip(range(len(arr)), range(len(arr)-1,-1,-1)):
#    print(arr[i][j])
