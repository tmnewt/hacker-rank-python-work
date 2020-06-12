import numpy as np

n = int(input())

arr1 = np.array([list(map(int, input().split())) for _ in range(n)])
arr2 = np.array([list(map(int, input().split())) for _ in range(n)])

print(np.dot(arr1, arr2))