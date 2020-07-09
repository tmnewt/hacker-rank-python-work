# https://www.hackerrank.com/challenges/zipped/problem

from statistics import mean

n, x = list(map(int, input().split()))

gradebook = [list(map(float, input().split())) for _ in range(x)]
grades = zip(*gradebook)
for g in grades:
    print(round(mean(g), 1))