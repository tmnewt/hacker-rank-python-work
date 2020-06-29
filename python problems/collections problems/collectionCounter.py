# https://www.hackerrank.com/challenges/collections-counter/problem

from collections import Counter

# Actual Problem


x = int(input())
shoes = Counter(list(map(int, input().split())))
c = int(input())

revenue = 0

for _ in range(c):
    size, p = list(map(int, input().split()))
    if shoes.get(size) == None:
        continue
    
    if shoes.get(size) != 0:
        revenue += p
        shoes.subtract([size])

print(revenue)

# example usage of Counter
exampleList = [1,1,2,3,4,5,3,2,3,4,2,1,2,3]
print(Counter(exampleList))
print(type(Counter(exampleList)))
print(list(Counter(exampleList).elements()))
print(Counter(exampleList).items())
print(Counter(exampleList).keys())
print(Counter(exampleList).values())
 
blob = Counter(exampleList)

print(blob.pop(1))
print(blob)
blob.update([2])
print(blob)
blob.subtract([3, 3, 3, 3, 3])
print(blob)
print(blob.get(7))


test = [[6, 55], [6, 40], [2, 100]]
for _, i in enumerate(test):
    print(i)



    
