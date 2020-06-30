# https://www.hackerrank.com/challenges/most-commons/problem?h_r=next-challenge&h_v=zen

from collections import Counter

s = input()

c = Counter(s)
commons = sorted(c.most_common(), key = lambda elm: (-elm[1], elm[0]))
for i in range(3):
    print(commons[i][0], commons[i][1])