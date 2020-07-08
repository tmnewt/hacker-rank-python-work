# https://www.hackerrank.com/challenges/merge-the-tools/problem

# this challenge has a terrible name

from collections import OrderedDict, Counter

class OrderedCounter(Counter, OrderedDict):
    # yes, the inheritance order matters
    pass


def merge_the_tools(string, k):
    for i in range(0, len(string), k):
        sub = string[i:i+k]
        print(''.join(OrderedCounter(sub).keys()))


test_string = 'L0LAABCAAADA'
test_k = 3
merge_the_tools(test_string, test_k)