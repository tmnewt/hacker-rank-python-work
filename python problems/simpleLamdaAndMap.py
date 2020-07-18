# https://www.hackerrank.com/challenges/map-and-lambda-expression/problem

cube = lambda x: x**3

def fibonacci(n):
    # O log n  because this is faster on incredibly large numbers
    # see: https://blog.paulhankin.net/fibonacci/
    def fibfast(n):
        n -= 1
        return (4 << n*(3+n)) // ((4 << 2*n) - (2 << n) - 1) & ((2 << n) - 1)
    if n == 0: return []
    if n == 1: return [0]
    fibs = [fibfast(i) for i in range(1,n)]
    fibs.insert(1,1) # because this problem uses [0,1,1] as the first 3 fibonacci
    return fibs

if __name__ == '__main__':
    n = int(input())
    print(list(map(cube, fibonacci(n))))

