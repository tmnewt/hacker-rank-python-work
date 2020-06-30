# https://www.hackerrank.com/challenges/word-order/problem

from collections import Counter

s = Counter([input() for _ in range(int(input()))])
print(len(s.keys()))
print(' '.join(list(map(str, s.values()))))


thing = ['bcdef', 'abcdefg', 'bcde', 'bcdef']
a = Counter(thing)
print(a)
print(len(a.keys()))
print(' '.join(list(map(str, a.values()))))