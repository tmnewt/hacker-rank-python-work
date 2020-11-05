# https://www.hackerrank.com/challenges/minimum-swaps-2/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

# determine the minimum number of swaps to sort an array in ascending order

# you could look up 'minimum operations to sort a random distinct elemnet array of n-length' but that would be no fun.

# Now, normally the answer to these problems comes from a mathematical property and 
# can be solved quickly with some clever shortcuts rather than attempting to brute force solve it.

# consider the following array. 
# [7, 1, 3, 2, 6, 4, 5, 9, 8, 10]


# If we consider the array to be 1-indexed (eww...) than any value which matches its index doesn't need to move.
# next we can search for index "pairs" which are values where when we swap them they will end in the correct final position 
# every count of these index "pairs" requires 1 swap operation.
# Lets use the symbol * to mark immediate pair swaps and & to mark values which do not need to be swapped.
# Start : [7, 1, 3, 2, 6, 4, 5, 9, 8, 10]
#         [7, 1, &, 2, 6, 4, 5, 9, 8, & ]  3 and 10 do not need to move
#         [7, 1, &, 2, 6, 4, 5, *, *, & ]  swap 9 and 8
#         [7, 1, &, 2, 6, 4, 5, 8, 9, & ]
#         [7, 1, &, 2, 6, 4, 5, &, &, & ]  mark off 8 and 9
#         [7, 1, &, 2, 6, 4, 5, ...
# 
# can anymore be immediately swapped? NO. We are left with 6 values that need to be rearranged. For simplicity lets ignore 8, 9, 10 because they don't matter anymore.
#         
#           [7, 1, &, 2, 6, 4, 5] 
# 
# Now you might be thinking, "How do I know that my approach to solving this part will produce the least swaps?"
# That's a good thing to be thinking about. Above, it's a lot easier to that for every index "pair" you will need 1 swap.
# So, using proof by exhaustion should help demonstate an underlying mathematical property
# The way to read the following is by picking a number and tracing what it swaps with next where it to swap the value that should be in it's current index.
# For instance
# 7 -> 1 -> 2 -> 4 -> 6 -> 5    means there are 5 swap operations that get 7 to it's index position while the value it is being swapped with ends up at its index position.
# 1 -> 7 -> 2 -> 4 -> 6 -> 5    here 1 was the staring number. Once it ends in it's index location the next active value becomes the last it was swapped with, in this case, 7.
# heres an exhaustive list of swap chains.
# 2 -> 1 -> 7 -> 4 -> 6 -> 5
# 4 -> 2 -> 1 -> 7 -> 

# aaaaaahhhh this is hard to demonstarte without graphs!!! The answer to this part is 5. It's always 1 less than the remaining number of unsorted values.

import numpy as np
import time

def minimumSwaps(arr):
    swaps = 0
    for i, value in enumerate(arr):
        while (i+1) != value:
            arr[i], arr[value-1], = arr[value-1], arr[i]
            value = arr[i]
            swaps += 1
    return swaps


def gg_minswaps_test(arr):
    n = len(arr)
    arrpos = [*enumerate(arr)]
    arrpos.sort(key = lambda it : it[1])
    vis = {k : False for k in range(n)}

    ans = 0
    for i in range(n):
        if vis[i] or arrpos[i][0] == i:
            continue
        cycle_size = 0
        j = i  
        while not vis[j]:
            vis[j] = True
            j = arrpos[j][0]
            cycle_size += 1
        if cycle_size > 0:
            ans += (cycle_size - 1)
    return ans

size = 10

array = np.random.choice(size, size, False)
array += 1
copy1 = np.copy(array)
copy2 = np.copy(array)

test = [7, 1, 3, 2, 6, 4, 5, 9, 8, 10]
print(minimumSwaps(array))
print(gg_minswaps_test(copy1))


