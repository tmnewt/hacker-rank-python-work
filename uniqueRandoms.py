
import random
import pandas as pd



def genUniqueRandom(samplesize, population):
    uniques = set()
    assert(samplesize <= population)
    while len(uniques) < samplesize:
        uniques.add(random.randint(0, population))
    return uniques


def closestNumbers(arr: set()):
    outs = []
    
    arr = sorted(arr) # return as sorted list
    diff = arr[1] - arr[0]
    for i in range(len(arr)-1): 
        if abs(arr[i+1]-arr[i]) < diff:
            diff = arr[i+1] - arr[i]
            outs = []
            outs.append(arr[i])
            outs.append(arr[i+1])
        elif abs(arr[i+1]-arr[i]) == diff:
            outs.append(arr[i])
            outs.append(arr[i+1])

    # don't do this...
    #for i in fungen:  ###
    #    if abs(arr[i+1]-arr[i]) == diff:
    #        outs.append(arr[i])
    #        outs.append(arr[i+1])
    return [diff, len(outs), (arr[-1]-arr[0])] 

draw_size = 200000
population = 40000000
results = []
for i in range(100):
    a = genUniqueRandom(draw_size, population)
    results.append(closestNumbers(a))
    print(f'\rdone with: {i+1}', end='')




# -10   to 10 
# -10, -7,  -5, -4, -3, 0, 10 

# for i in range(1, len(arr)):  ###
#       
#        if abs(arr[i]-arr[i-1]) < diff:

