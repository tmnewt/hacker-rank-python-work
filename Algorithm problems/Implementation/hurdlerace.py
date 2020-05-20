def hurdleRace(k: int, heights: list):
    if k >= max(heights):
        return 0
    return (max(heights)-k)

