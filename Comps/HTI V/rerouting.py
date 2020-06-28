# if a value equals it's 1-indexed index then the node is referencing itself
# example: [1, 2, 3, 4]
# otherwise think of the index as the node and its value as the pointer to the next node (based on 1-indexed)
# example: [2, 3, 4, 1, 5]
# is 1(2) -> 2(3) -> 3(4) -> 4(1) with 5 by itself
# making 1 change here is the minimum amount of work
# could have 5(n but not 5) or 4(5)

# another example [3, 3, 3, 4, 4, 4] 
# is node 1 and 2 lead to 3 and 3 leads to itself 
# meanwhile nodes 5 and 6 lead to 4 and 4 leads to itself.

# if none are linked then the minimum is always n - 1 

import numpy as np

def getMinConnectionChange(connections: list):
    if len(connections) == 0:
        return 0
    
    memo = [0] * len(connections)
    compCount = 0
    for i in range(len(connections)):        
        if memo[i] != 0: continue  # end this increment

        startIndex = i + 1 
        current = i 
        pointer = connections[current] - 1 
        
        while True:
            if memo[current] == startIndex: # found a component loop or itself.
                compCount += 1
                break
            elif memo[current] != 0: # found an existing component
                break
            
            memo[current] = startIndex
            current = pointer
            pointer = connections[current] - 1
        
    return compCount-1

def getMinConnectionChangeText(connections: list):
    # I think the best approach here is to identify components and then the solution will be c-1 
    # the issue is efficiently 
    memo = [0] * len(connections)
    compCount = 0
    for i in range(len(connections)):
        print(f'evaluating index {i+1} which contains {connections[i]}')
        if memo[i] != 0:
            print(f'{connections[i]} is part of a component') 
            continue
        else: print(f'node {i+1}\'s connections hav not been traced. Tracing now.')

        startIndex = i + 1
        current = i 
        pointer = connections[current] - 1 
        while True:
            print(f'current node: {current+1} points to {connections[current]}')
            if memo[current] == startIndex:
                compCount += 1
                print(f'identified componet. compCount = {compCount}')
                break
            elif memo[current] != 0:
                print('reached an existing component')
                break
            memo[current] = startIndex
            current = pointer
            pointer = connections[current] - 1
        
    return compCount-1



#index=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22,  23]
test = [2, 1, 4, 5, 5, 7, 8, 9, 10, 9, 15, 15, 15, 15, 15, 15, 15, 15, 15, 21, 22, 20,  14, 24] 
# comps [ 1 ] [   2  ] [     3,      ] [                4                ] [    5    ]  [4] [6]
# 5 components in the above test. 

test = list(np.random.randint(1, 300000, 300000))
print(getMinConnectionChange(test))

blob = [n+1 for n in range(10)]
print(blob)
print(getMinConnectionChangeText(blob))

print(getMinConnectionChange([1,2,3]))