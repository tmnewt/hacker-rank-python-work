arr = [1,3,5,7,9]

minimum = sum(arr)
maximum = 0



# sliding slice
for i in range(5):
    calc = arr[:i]+arr[i+1:]
    x = sum(calc)
    if x < minimum:
        minimum = x
    if x > maximum:
        maximum = x

print(f'{minimum} {maximum}')

# start slicing
# take the first 4, so          [# , # , # , # , ig]
# move slicer 1 index over, so  [ig, # , # , # , # ]
# move over again               [# , ig, # , # , # ]
# again,                        [# , # , ig, # , # ]
# again,                        [# , # , # , ig, # ]
# and we reach the start so we are done.

# We can think of this pattern a 2 slices of 2. 1 slice exists
# before the value we want to ignore, and the other slice 
# exists behind the value we want to ignore.
# 
# so that means,
#    arr[2:4]+arr[0:2]
# 
# is the exact same thing as,
#    arr[0:4]
#
# why think about it in this way? Because it is more robust
# than thinking about it as one whole slice.


#print(arr[0:2] + arr[2:4])
#print(arr[1:3] + arr[3:5])
#
#space = arr[2:5]
#space.append(arr[0])
#print(space)
#
#print(arr[0:2]+arr[3:5])
#space = arr[0:3] 
#space.append(arr[-1])
#print(space)

