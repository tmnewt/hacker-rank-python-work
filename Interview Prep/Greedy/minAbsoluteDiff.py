# https://www.hackerrank.com/challenges/minimum-absolute-difference-in-an-array/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=greedy-algorithms

def minimumAbsoluteDifference(arr):
    arr.sort()
    minimum = 10**10
    for i in range(len(arr)-1):
        if (arr[i+1] - arr[i]) < minimum:
            minimum = (arr[i+1] - arr[i])

    return minimum

