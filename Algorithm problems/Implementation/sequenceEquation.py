# https://www.hackerrank.com/challenges/permutation-equation/problem?h_r=internal-search

# given sequence of distinct integers
# For each x where 1<= x <= n, find any int y such that p[p[y]] === x
# 
# for example assume the sequence [5, 2, 1, 3, 4]
# 
# start with x = 1 and count up to 5.
#
# what value y will return 1 when run through p[p[y]]
# The answer is 4
# reasoning: p[4] = 3, so then p[3] = 1
# 
# in an 1-indexed array the first value would be 1
# 
# so p[] is a one-to-one function (because of the distinct property above) 
# so each unique input has only 1 unique output.
# therefor p[y] = x can be inverted

test = [5, 2, 1, 3, 4]
# x = 1 === p[3] and p[4] = 3 so p[p[4]] = 1
# x = 2 === p[2] and p[2] = 2 so p[p[2]] = 2
# x = 3 === p[4]

def permutationEquation(p: list):
    inverted = [p.index(x)+1 for x in range(1, len(p)+1)]
    return [p.index(x)+1 for x in inverted]

def invertList(p: list):
    return [p.index(x)+1 for x in range(1, len(p)+1)]

#spam = invertList(test)
#print(invertList(spam))
print(permutationEquation(test))

test2 = [2, 3, 1]
print(permutationEquation(test2))

test3 = [4, 3, 5, 1, 2]
print(permutationEquation(test3))

