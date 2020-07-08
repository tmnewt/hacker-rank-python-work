'''Union'''
# https://www.hackerrank.com/challenges/py-set-union/problem

testS1 = set([1,2,3,4,5,6,7,8,9])
testS2 = set([10,1,2,3,11,21,55,6,8])

n1 = int(input())
s1 = set(map(int, input().split()))
n2 = int(input())
s2 = set(map(int, input().split()))

u = s1.union(s2)
print(len(u))


'''Intersection'''
# https://www.hackerrank.com/challenges/py-set-intersection-operation/problem?h_r=next-challenge&h_v=zen

print(len(s1.intersection(s2)))


'''Difference'''
# https://www.hackerrank.com/challenges/py-set-difference-operation/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

print(len(s1.difference(s2)))

'''Symmetric Difference'''
# https://www.hackerrank.com/challenges/py-set-symmetric-difference-operation/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

print(len(s1.symmetric_difference(s2)))