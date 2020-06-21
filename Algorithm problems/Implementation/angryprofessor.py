# https://www.hackerrank.com/challenges/angry-professor/problem


def angryProfessor(k: int, a: list):
    ontime = 0
    for i in a:
        if i <= 0:
            ontime += 1
    if ontime >= k:
        return 'NO'
    return 'YES'
    