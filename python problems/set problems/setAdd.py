# https://www.hackerrank.com/challenges/py-set-add/problem

n = int(input())

s = set()
for _ in range(n):
    a = input()
    s.add(a)

print(len(s))