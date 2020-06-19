# https://www.hackerrank.com/challenges/mark-and-toys/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting&h_r=next-challenge&h_v=zen


def maximumToys(prices: list, k: int):
    prices.sort()
    total = 0
    i = 0
    count = 0
    size = len(prices)-1
    while (total <= k) and i != size:
        if (total + prices[i]) > k:
            break
        
        total += prices[i]
        i += 1
        count += 1
    
    return count

test = [7, 6, 1, 2, 3, 4, 3]

print(maximumToys(test, 13))