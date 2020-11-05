# https://www.hackerrank.com/challenges/two-strings/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps

# The easiest solution is to use the & operator to find the intersection
from collections import Counter

def testfunc(s1, s2):
    c1 = Counter(s1)
    c2 = Counter(s2)
    #print(c1)
    #print(c2)
    #addition = c1 + c2
    #print(addition)
    subtraction = c1 - c2
    #print(subtraction)
    print(subtraction-c1 == {})

def twoStrings(s1, s2):
    a = set(s1)
    b = set(s2)
    if a & b:
        return 'YES'
    else:
        return 'NO'

test1 = 'omgnoway'
test2 = 'iknoywright'

#testfunc(test1, test2)
print(twoStrings(test1, test2))
