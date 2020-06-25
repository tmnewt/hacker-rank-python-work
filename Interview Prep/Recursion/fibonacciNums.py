# https://www.hackerrank.com/challenges/ctci-fibonacci-numbers/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=recursion-backtracking

# pure recursion solution (disgusting...)
def fibonacciR(n):
    if n in [0,1]: return n
    else: return fibonacciR(n-1) + fibonacciR(n-2)

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

print(fibonacci(39))
print(fibfast(39))