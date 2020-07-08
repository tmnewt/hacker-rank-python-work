# https://www.hackerrank.com/challenges/py-check-strict-superset/problem?h_r=next-challenge&h_v=zen

'''Recall subset definitions

Set A is a subset of set B, if A is contained in B.
Equivalently B is a superset of A, if A is contained in B.
B is a strict superset if it is a superset and 
 contains 1 element which is not an element of A.

Recall 2 properties of subsets:
Property 1
Set A is a subset of B if and only if their union is equal to B

Property 2
Set A is a subset of B if and only if their intersection is equal to B.


Extending this logic, if A union B equals B, and len(A intersection B) < len(B)
then B is a strict superset.
'''

a = set(map(int, input().split()))
n = int(input())
answer = True
for _ in range(n):
    s = set(map(int, input().split()))
    if (s.union(a) == a) and (len(s.intersection(a)) < len(a)):
        pass
    else:
        answer = False

print(answer)




#testA = set([1,2])
#testB = set([1,2,4,5,6])
#
#print(testA.intersection(testB))
#print(testA.union(testB))
