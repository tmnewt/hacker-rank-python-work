# https://www.hackerrank.com/challenges/new-year-chaos/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

# suppose there is 1-based index of distinct n-length array. Array values initialized as [1, 2, 3, ... , n] 
# This array describes a que.
# The front of the que is the left most position.
# The values of the que at the start are the positions of a person in the que.
# A person may bribe the person directly in front of them to swap.
# A person may only bribe someone else at most 2 times.
# given the final state of the array, calculate the minimum number of swaps to get to this state.
# Assume that some final states provided may be invalid as it would require a value to have been swapped more than 2 times.
#   In such a case flag the given state as invalid.

# At first I thought this was more challenging than it actually was. 
#   I originally missed the rule of only swapping with the 
#   person in front of them, and thought they could swap with 
#   anyone in the que (which is a whole different problem) 
#
# Given the rule about swapping only with the person in front of them,
#   and the rule that a person can only bribe someone else twice, (there
#   is no rule about receiving bribes), this makes for a much simplier
#   problem than I imagined.
# 
# It might be tempting to look for values that are more than 2 indexes from their
#   associate starting point, but that wouldn't cover cases where a person near the
#   the front of the que was consecutively bribed to the back. 
#   For instance, [3,2,5,4,6,7,8,9,10,1] would be valid because person 1 ended at
# the back after receiving bribes.
#   Proof
#   [3, 2, 5, 4, 6, 7, 8, 9, 10, 1]
#   Steps  
#   [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
#   [2, 1, 3, 4, 5, 6, 7, 8, 9, 10]
#   [2, 3, 1, 4, 5, 6, 7, 8, 9, 10]
#   [3, 2, 1, 4, 5, 6, 7, 8, 9, 10]
#   [3, 2, 1, 5, 4, 6, 7, 8, 9, 10]
#   [3, 2, 5, 1, 4, 6, 7, 8, 9, 10]
#   [3, 2, 5, 4, 1, 6, 7, 8, 9, 10]
#   [3, 2, 5, 4, 6, 1, 7, 8, 9, 10]
#   [3, 2, 5, 4, 6, 7, 1, 8, 9, 10]
#   [3, 2, 5, 4, 6, 7, 8, 1, 9, 10]
#   [3, 2, 5, 4, 6, 7, 8, 9, 1, 10]
#   [3, 2, 5, 4, 6, 7, 8, 9, 10, 1]
# sure would be nice if I had a tool that could generate walking you through these steps...
# (is it easier to find a nice logical trick that holds true, or to brute force it upfront?...)
# so if a value - current_index > 2 then it is invalid.
# some obvious things to rule out are bribing the person in front of you only to then accept a bribe from the person you just bribed (this adds more swaps)
# as for finding the minimum number of swaps (what we are here to do,) we use the following approach
# take the given final que and attempt to move all values back to their original positions using 
# the above rules.
# So remember there is directionality to the problem rules.
# We can swap higher numbers with lower numbers and count that as a bribe. but only twice.
# once we've exhausted that we move on. If we reach the end of this process and not everything
# is sorted then the array was impossible to begin with.
# 
# Consider a the array above
#            Result of operation            i       Instruction for next           Bribe count after operation
#Given: [3, 2, 5, 4, 6, 7, 8, 9, 10, 1]     i = 0   Swap 3, 2                      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
#       [2, 3, 5, 4, 6, 7, 8, 9, 10, 1]     i = 1   Nothing because 3 < 5          [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
#       [2, 3, 5, 4, 6, 7, 8, 9, 10, 1]     i = 2   Swap 5, 4                      [0, 0, 1, 0, 0, 0, 0, 0, 0, 0]
#       [2, 3, 4, 5, 6, 7, 8, 9, 10, 1]     i = 3   Nothing because 5 < 6          [0, 0, 1, 0, 1, 0, 0, 0, 0, 0]
#       [2, 3, 4, 5, 6, 7, 8, 9, 10, 1]     i = 4   Nothing because 6 < 7          [0, 0, 1, 0, 1, 0, 0, 0, 0, 0]
#       [2, 3, 4, 5, 6, 7, 8, 9, 10, 1]     i = 5   Nothing because 7 < 8          [0, 0, 1, 0, 1, 0, 0, 0, 0, 0]
#       [2, 3, 4, 5, 6, 7, 8, 9, 10, 1]     i = 6   Nothing because 8 < 9          [0, 0, 1, 0, 1, 0, 0, 0, 0, 0]
#       [2, 3, 4, 5, 6, 7, 8, 9, 10, 1]     i = 7   Nothing because 8 < 9          [0, 0, 1, 0, 1, 0, 0, 0, 0, 0]
#       [2, 3, 4, 5, 6, 7, 8, 9, 10, 1]     i = 8   Nothing because 9 < 10         [0, 0, 1, 0, 1, 0, 0, 0, 0, 0]
#       [2, 3, 4, 5, 6, 7, 8, 9, 10, 1]     i = 9   swap 10 and 1                  [0, 0, 1, 0, 1, 0, 0, 0, 0, 1]
#       [2, 3, 4, 5, 6, 7, 8, 9, 1, 10]     i = 8   swap 9 and 1                   [0, 0, 1, 0, 1, 0, 0, 0, 0, 1]
#       [2, 3, 4, 5, 6, 7, 8, 1, 9, 10]     i = 7   swap 8 and 1                   [0, 0, 1, 0, 1, 0, 0, 0, 1, 1]
#       [2, 3, 4, 5, 6, 7, 1, 8, 9, 10]     i = 6   swap 7 and 1                   [0, 0, 1, 0, 1, 0, 0, 1, 1, 1]
#       [2, 3, 4, 5, 6, 1, 7, 8, 9, 10]     i = 5   swap 6 and 1                   [0, 0, 1, 0, 1, 0, 1, 1, 1, 1]
#       [2, 3, 4, 5, 1, 6, 7, 8, 9, 10]     i = 4   swap 5 and 1                   [0, 0, 1, 0, 1, 1, 1, 1, 1, 1]
#       [2, 3, 4, 1, 5, 6, 7, 8, 9, 10]     i = 3   swap 4 and 1                   [0, 0, 1, 0, 2, 1, 1, 1, 1, 1]
#       [2, 3, 1, 4, 5, 6, 7, 8, 9, 10]     i = 2   swap 3 and 1                   [0, 0, 1, 1, 2, 1, 1, 1, 1, 1]
#       [2, 1, 3, 4, 5, 6, 7, 8, 9, 10]     i = 1   swap 2 and 1                   [0, 0, 1, 1, 2, 1, 1, 1, 1, 1]
#       [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]     i = 0   done!                          [0, 1, 1, 1, 2, 1, 1, 1, 1, 1]
#
# we can see how iterating back and forth would be an effective tactic. but I think this confirms a thought I had about checking
# 
# damn, I've written so much but I just want to move on from this problem
# Heres an example that doesn't work
# [5, 4, 1, 6, 3, 2]
# 5 could not have reached its final location without bribing more than twice

import numpy as np

test = [1, 4, 7, 2, 6, 5, 3]
test2= [3, 2, 5, 4, 6, 7, 8, 9, 10, 1]
def minimumBribes_too_slow(que):
    # I hate 1-based indexing...
    swaps = 0
    for index, value in enumerate(que):
        # if a value (0-based) occupies an index that is more than 2 from starting index (it's value (0-based)) then it bribed more than 2 people.
        if (value - 1) > index + 2:
            print('Too chaotic')
            return
        # else infer the number of bribes by looking at everything in front if the current index and counting instances of values bigger than the value in question.
        for i in range(index):
            if que[i] > value:
                swaps += 1
    print(swaps)
    
def minimumBribes_with_output(que):
    # I hate 1-based indexing...
    swaps = 0
    for index, value in enumerate(que):
        # if a value (0-based) occupies an index that is more than 2 from starting index (it's value (0-based)) then it bribed more than 2 people.
        if (value - 1) > index + 2:
            print('Too chaotic')
            return
        # else infer the number of bribes by looking at values in in front of the 
        # current index and counting instances of values bigger than the value in question.
        # to save time, the range can start from the 0-based index of the value in question.
        # but be sure to subtract 2 from the value (1 because of 1-based and 1 to reach the index in front)
        if not value-2 < 0:
            start = value-2
        else:
            start = 0
        mini_list = []
        for i in range(start, index):
            tup = (que[i], False, i)
            if que[i] > value:
                tup = (que[i], True, i)
                swaps += 1
            mini_list.append(tup)
        if mini_list:
            print(mini_list)
    print(swaps)


def minimumBribes(que):
    # I hate 1-based indexing...
    swaps = 0
    for index, value in enumerate(que):
        # if a value (0-based) occupies an index that is more than 2 from starting index (it's value (0-based)) then it bribed more than 2 people.
        if (value - 1) > index + 2:
            print('Too chaotic')
            return
        # else infer the number of bribes by looking at values in in front of the 
        # current index and counting instances of values bigger than the value in question.
        # to save time, the range can start from the 0-based index of the value in question.
        # but be sure to subtract 2 from the value (1 because of 1-based and 1 to reach the index in front)
    #   if not value-2 < 0:
    #       start = value-2
    #   else:
    #       start = 0
        # that's the same as max()!!!!!
        start = max(value-2, 0)
        for i in range(start, index):
            if que[i] > value:
                swaps += 1
    print(swaps)





#size = 20
#forwards = np.arange(1, size+1) 
#backwards = np.flip(forwards)
#forwards = list(forwards)
#backwards = list(backwards)


minimumBribes_too_slow(test)
minimumBribes_too_slow(test2)
minimumBribes_with_output(test)
minimumBribes_with_output(test2)

minimumBribes(test)
minimumBribes(test2)


    