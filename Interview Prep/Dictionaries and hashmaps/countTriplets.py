
# I am so dumb. I completely forgot that we have 3 r constants in the form of 
#  v
#  v* r
#  v * r^2
#  
# 
# R is given at the beginning so we can know ahead of time r, r^2, and r^3.

# Now remember the nth term of a geometric sequence is defined as
#
#               v * r^(n-1)
#
# breaking these out into components by nth terms gives us.
#   Component 1:    v    =  v * r (1-1) 
#   Component 2:   v*r   =  v * r (2-1) 
#   Component 3:  v*r^2  =  v * r (3-1) 
#
# Now for a given value we don't know which component it is. 
# So we have to logically determine that using prior information.
#
# Now, I will lay out the following instructions but the way they are implemented
# is in the exact opposite order they are displayed.
#
# 1)
# For a given in the array multiply it by r and use the product as a 
#   key for a dictionary.
#       For newly added keys set their initial value to 1
#       If the key already exists, increment its value by 1
#
#   Now, this dictionary will keep a count of all instances where the PRIOR value 
#       of the geometric sequence existed. Think of this as the memory of the
#       for determining the first 2 parts of a geometric sequence.
#   (below I use a counter collection obj instead of a dictionary but it can essentially
#    thought of as a dictionary. It bassically does incrementing for me)
# 
#   Lets call this dictionary the second value dictionary, but remember, what each key
#   tracks are the instances when the key's geometric 'prior' caused 
#   the key's stored value to increment. 
#
#2). 
# We see if the value in question is in the second values dictionary. If it is
#   multiply the value by r and use the product as a key for the 3rd value dictionary.
#   Increment the count for this key by the amount of counts in second_values[value] 


# god, this is so hard to explain...


import os
from collections import Counter


def countTriplets(arr, r):
    # kill me, this was hard.
    count = 0
    third_values = Counter()
    second_values = Counter()
    for value in arr:
        if value in third_values:
            count += third_values[value]
        if value in second_values:
            third_values[value*r] += second_values[value]
        second_values[value*r] += 1
    return count

test = [1, 3, 9, 9, 27, 81]
print(countTriplets(test,3))




#
#
test = '1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1'
test = test.split()
print(countTriplets(test, 1))


for file in os.listdir():
    if file[-3:] == 'txt':
        with open(file, 'r') as f:
            lines = f.readlines()
        junk , ratio = list(map(int, lines[0].split()))
        test = list(map(int, lines[1].split()))
        print(countTriplets(test, ratio))