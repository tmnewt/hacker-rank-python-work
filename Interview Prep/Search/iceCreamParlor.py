# https://www.hackerrank.com/challenges/ctci-ice-cream-parlor/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=search


# this is a sum of pairs a + b = c
# therefor a = c-b  &  b = c-a will speed things up.

def whatFlavors(costs, money):
    flavors = []
    table = dict()
    for i, cost in enumerate(costs):
        if cost not in table:
            # pretend the current flavor is the one to be picked.
            # use the remaining value as the key
            table[money-cost] = i+1
        
        else: # the cost has occured 'again'
            flavors.append(i+1)
            flavors.append(table[cost])
            break
    flavors.sort()
    print(flavors[0], flavors[1])

whatFlavors([1, 4, 5, 3, 2], 4)