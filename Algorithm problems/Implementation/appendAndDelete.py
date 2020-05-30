# s = original string
# t = newstring
# using only 2 operations (1. append to end  2. remove from end)
# determine if the original string can be changed to the newstring in exactly k operations

# example
# old string = "tell"
# new string = "tellers"
# if k = 2 then return "no" the operation cannot be done in exactly 2 moves
# if k = 3 then return "yes" 

# first create iterable code. See if iteration is all we need,
# optimize later (if needed)

def appendAndDelete(s: str, t: str, k: int):
    fronting = 0
    for i in range(min(len(s), len(t))):
        if s[i] == t[i]:
            fronting += 1
        else:
            break
    if k >= len(s) + len(t):
        return 'Yes'
    elif k < len(s)-fronting + len(t)-fronting:
        return 'No'
    else:
        if (k-(len(s)-fronting+ len(t)-fronting))%2 == 0:
            return 'Yes'
        return 'No'

oldstring = 'CptLocke'
newstring = 'CptDis'
k = 14  # return no

# 
# define fronting as substring matching elements that 1 for 1 matches
#           from the 0-index 
# Therefor fronting is what doesn't need to change.
# if there is no fronting, everything needs to change.
#       Because of the repeatability of removing from an empty string,
#       in the case of no fronting, any k >= len(old) + len(new)
#       will work. Actually that's true regardless of what the fronting is

# where k < len(old)-fronting + len(new)-fronting then it's not possible.

# if k is between the upper bound and the lower bound then
#         if (k - lowerbound)%2 == 0, then return Yes
#          else.. return no

print(appendAndDelete(oldstring, newstring, k))

old = 'ashley'
new = 'ash'
test = 2

print(appendAndDelete(old, new, test))

# failed test cases
old = 'y'
new = 'yu'
k = 2
print(appendAndDelete(old, new, k))