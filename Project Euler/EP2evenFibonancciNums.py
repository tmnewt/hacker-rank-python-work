# https://www.hackerrank.com/contests/projecteuler/challenges/euler002/problem

# messing around first

fibs = [1,2]

for i in range(200):
    fibs.append(fibs[-1]+fibs[-2])


evens = [ i for i in fibs if i%2 == 0]
print(evens)