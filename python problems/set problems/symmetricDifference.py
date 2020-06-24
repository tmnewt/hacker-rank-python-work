# https://www.hackerrank.com/challenges/symmetric-difference/problem

m = int(input())
line1 = set(map(int, input().split()))
n = int(input())
line2 = set(map(int, input().split()))

result = line1.union(line2)
intersect = line1.intersection(line2)
for i in intersect:
    result.discard(i)

result = list(result)
result.sort()

for i in result:
    print(i)