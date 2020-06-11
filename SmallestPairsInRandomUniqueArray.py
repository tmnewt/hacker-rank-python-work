import os
import numpy as np
import time

def closestNumbers(arr, fungen):
    arr = np.sort(arr)
    diff = abs(max(arr)-min(arr))
    for i in fungen:
        if abs(arr[i+1]-arr[i]) < diff:
            diff = arr[i+1] - arr[i]
    outs = []
    for i in fungen:
        if abs(arr[i+1]-arr[i]) == diff:
            outs.append(arr[i])
            outs.append(arr[i+1])
    return [diff, len(outs), np.median(np.array(outs))]


start_time = time.time()

draw_size = 200000
fungen = range(draw_size-1)
drawgen = range(40000001)
results = []
for i in range(10):
    a = np.random.choice(drawgen, draw_size)
    workings = closestNumbers(a, fungen)
    results.append([abs(max(a)-min(a)), workings[0], workings[1], np.mean(a), workings[2], np.std(a)])
    print(f'done with: {i+1}')
print(time.time() - start_time)
print(results)

