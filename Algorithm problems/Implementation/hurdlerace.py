# https://www.hackerrank.com/challenges/the-hurdle-race/problem?h_r=internal-search

def hurdleRace(k: int, heights: list):
    if k >= max(heights):
        return 0
    return (max(heights)-k)

