# https://www.hackerrank.com/challenges/cats-and-a-mouse/problem?h_r=internal-search

# 1 dimension linear
# 3 ints on the line. Line length under 100.
# mouse can't move
# return string of either 'Cat A', 'Cat B', or 'Mouse C'

def catAndMouse(x, y, z):
    cam = abs(z-x)
    cbm = abs(z-y)
    if cam == cbm:
        return 'Mouse C'
    if cam > cbm:
        return 'Cat B'
    if cbm > cam:
        return 'Cat A'

print(catAndMouse(10, 11, 2))