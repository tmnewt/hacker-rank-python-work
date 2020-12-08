# https://www.hackerrank.com/challenges/pairs/problem


# start by sorting the elements.
# go element by element. 
# jump to index j near the middle of the list.
# evaluate the difference of list[j] - list[i] 
#   if the difference is less than K,    take the right hand side of list split on index j.
#   if the difference is greater than K, take the left  hand side of list split on index j
#   if no difference, pop the element at index i.

# actually it would make sense to work from the back in that case.. whatever.
# #

# actually, since all elements are guaranteed to be unique, using sets will speed this
# up. 

def pairs(k, arr):
    set_arr = set(arr)
    set_arr_k_large = {s+k for s in set_arr}
    return len(set_arr & set_arr_k_large)




test = [2, [1, 5, 3, 4, 2]]
print(pairs(*test))
