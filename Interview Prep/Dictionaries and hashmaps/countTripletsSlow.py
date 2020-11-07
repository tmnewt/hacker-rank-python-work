# https://www.hackerrank.com/challenges/count-triplets-1/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

# going to identify some geometric progressions!
#  https://en.wikipedia.org/wiki/Geometric_progression

# given an array find all triplets of indices (i, j, k) such that the values at these indices are in geometric progression for a given common ratio, r.
# Rules:
#    the common ratio r  is a positive integer between 1 and 10^9
#    a pattern follows that  i < j < k

# I'm thinking we can take advantage of the mathematical property:  
#      nth term of a geometric sequence is 
#
#               a * r^(n-1)
#
#      where a = the starting value(here, i), and r = the common ratio 
#
# in this way, we can know ahead of time what other values will accompany our starting value, a.
# We cannot use 2 loops because the size of the array may be as big as 10^9
# I'm thinking making a dictionary of values as the key with their index in the array being a list of indexes of the value.
# This way we loop once. 

# Then loop again. take the value of i index
# the next geometric value will be value * r. Assign this as value_2
# check if this value is a key of the dictionary (if not, continue to next iteration)
# the next geometric value will be value_2 * r. Assign this as value_3
# check if this value is a key of the dictionary (if not, continue to next iteration)
# (by the way, the value at i is guaranteed to be in the dictionary if that wasn't clear...)
#
# In the value_2 inner list, popleft any indexes that are smaller than i
#   Do so until you hit an index greater than i. that means the 2nd value in the geometric sequence has been found (do not pop that index)
#   record that index as j.
# In the value_3 inner list, popleft any indexes that are smaller than i
#   Do so until you hit an index greater than i.
#   Then continue until you reach an index greater than j.
#   that means the 3rd value in the geometric sequence has been found (do not pop that index)
# At this point you have found a geometric series triplet. 
# before continuing to the next iteration go to value key in dictionary and popleft the 1st index (this should be the same index as i)
import os

from collections import deque as deck

def countTripletsSlow(arr:list, r):
    count = 0
    triplets = dict()
    # loop to build dictionary
    for i, value in enumerate(arr):
        try:
            triplets[value].append(i)
        except KeyError:
            triplets[value] = deck([i])
    # loop to solve problem (skip early to save processing time)
    for i, value in enumerate(arr):
        #print(value)
        #print(triplets)
        triplets[value].popleft()
        value_2 = value * r
        if value_2 not in triplets:
            continue
        value_3 = value_2 * r
        if value_3 not in triplets:
            continue
        #print(value, value_2, value_3)
        try:
            while triplets[value_2][0] < i:
                triplets[value_2].popleft()
        except IndexError:
            del triplets[value_2]
            continue
        try:
            while triplets[value_3][0] < i:
                triplets[value_3].popleft()
        except IndexError:
            del triplets[value_3]
            continue
        #js = len([j if i < j for j in triplets[value]  ]
        #count += len(triplets[value_2]) * len(triplets[value_3])
        for j in triplets[value_2]:
            count += len([k for k in triplets[value_3] if j<k])
                #if j < k:
                #    #print((i,j,k))
                #    count += 1
    #print(triplets)
    return count



#test = [1, 3, 9, 9, 27, 81]
test_list = [1, 125, 5, 5, 25, 125]
test_r = 5
print(countTripletsSlow(test_list, test_r))

test = '1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1'
test = test.split()
print(countTripletsSlow(test, 1))



for file in os.listdir():
    if file[-3:] == 'txt':
        with open(file, 'r') as f:
            lines = f.readlines()
        junk , ratio = list(map(int, lines[0].split()))
        test = list(map(int, lines[1].split()))
        print(countTripletsSlow(test, ratio))


#special = deck(test_list)
#special.popleft()
#special.popleft()
#print(type(special))
#print(special)

#test_dict = dict()
#test_dict[0] = {}
#test_dict[0][1] = 'am I allowed to do this?'
#print(test_dict)
# yes!