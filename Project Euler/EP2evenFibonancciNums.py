# https://www.hackerrank.com/contests/projecteuler/challenges/euler002/problem

# use memoization to save time.
# or use: https://blog.paulhankin.net/fibonacci/

# memoization
def fibonacci(num: int):
    memo = [0,1]
    def fibIn(n):
        if len(memo) > n:  # consider rearranging the conditional statement
            return memo[n]
        fibIn(n-1)
        memo.append(memo[n-1]+memo[n-2])
        return memo[n]
    return fibIn(num)


# O log n 
# see: https://blog.paulhankin.net/fibonacci/
def fibfast(n):
    n -= 1
    return (4 << n*(3+n)) // ((4 << 2*n) - (2 << n) - 1) & ((2 << n) - 1)


class fiboe:
    
    def __init__(self):
        self.evens = [0,2,8]
        #self.sums = 
        #self.highest

    def nextevenfib(self):
        pass
        





for _ in range(10000):

    n = 4*(10**16)

    evens = []
    highest = 0
    i = 1
    while highest <= n:
        fib = fibfast(i)
        if fib > n:
            break
        if fib%2 == 0:
            evens.append(fib)
        highest = fib
        i += 1

print('done')


# wow, the above is still not fast enough.

# ok, so every 3rd term of the series is even.

# in fact, E(n) = 4 * E(n-1) + E(n-2)

