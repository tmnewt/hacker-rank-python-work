# https://www.hackerrank.com/challenges/divisible-sum-pairs/problem?h_r=internal-search

k = 3
ar = [1, 3, 2, 6, 1, 2]

count = 0
for i in range(len(ar)):
    for j in range(i+1, len(ar)):
        if ((ar[i]+ar[j])%3) == 0:
            count += 1
print(count)

# submission.

#def divisibleSumPairs(n, k, ar):
#    count = 0
#    for i in range(n):
#        for j in range(i+1, n):
#            if (ar[i]+ar[j])%k == 0:
#                count += 1
#    return count