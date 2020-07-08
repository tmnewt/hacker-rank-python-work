# https://www.hackerrank.com/challenges/py-check-subset/problem

'''Recall these properties of subsets
Property  1:
Set A is a subset of B if and only if their intersection 
is equal to B.

Property 2:
Set A is a subset of B if and only if their union is equal to B


Here we are interested in property 2
'''

n = int(input())
for _ in range(n):
    ln1 = int(input())
    a = set(map(int, input().split()))
    ln2 = int(input())
    b = set(map(int, input().split()))
    if a.union(b) == b:
        print('True')
    else:
        print('False')

# examples:
#testA = set([1,2])
#testB = set([1,2,4,5,6])
#
#print(testA.intersection(testB))
#print(testA.union(testB))
