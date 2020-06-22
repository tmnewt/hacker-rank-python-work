# https://www.hackerrank.com/challenges/ctci-array-left-rotation/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=arrays

test = [1, 3, 4, 5, 8, 11, 12, 15]
n = 7

def rotLeft(a: list, d: int):
    d = (d%(len(a)))
    return a[d:] + a[:d]

print(rotLeft(test, n))
