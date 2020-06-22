# https://www.hackerrank.com/challenges/birthday-cake-candles/problem?h_r=internal-search

arr = [4,2,6,4,3,8,8,8]

tallest = max(arr)

b = 0
for i in arr:
    if i == tallest:
        b += 1

print(b)