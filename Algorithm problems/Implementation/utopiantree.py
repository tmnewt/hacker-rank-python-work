# https://www.hackerrank.com/challenges/utopian-tree/problem?h_r=internal-search

def utopianTree(n):
    height = 1
    for i in range(n):
        if i%2 == 1:
            height += 1
        else:
            height = height * 2
    return height

print(utopianTree(5))