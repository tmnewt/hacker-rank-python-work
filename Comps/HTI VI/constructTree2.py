import math

def depthscore(n):
    return ((n+1)*n)//2

def scores(l):
    score = 0
    for i in l:
        score += depthscore(i)
    return score

def flatten(a, b):
    remainder = a%b
    if remainder == 0:
        score = b*depthscore(a//b)
    else:
        diff = b-remainder
        peak = (a+diff)//b
        score = (b-1)*depthscore(peak)+depthscore(peak-diff)
    return score

def flatbox(a,b):
    remainder = a%b
    if remainder == 0:
        tmp = []
        peak = a//b
        for i in range(b):
            tmp.append(peak)
    else:
        diff = b-remainder
        peak = (a+diff)//b
        tmp = []
        for i in range(b):
            tmp.append((a+diff)//b)   
        tmp[-1] = tmp[-1]-diff
    return tmp

def findOptBranches(N, X):
    a = N-1
    guess = flatten(a, 2)
    upperbranch = 2
    lowerbranch = 1
    while True:
        if guess == X:
            lowerbranch += 1
            break
        if guess < X:
            break
        else: # x < guess
            upperbranch +=1
            lowerbranch +=1
            guess = flatten(a, upperbranch)

    print('upperbranch', upperbranch)
    print('lowerbranch', lowerbranch)
    print('last guess:', guess)
    #print('diff: ', X-guess)
    return [upperbranch, lowerbranch, guess]





data = []

def findMaxdepth(nodes, target):
    if (nodes-1 > target) or (target > ((nodes*(nodes-1))/2)):
        #print('throw out')
        return [[-1, -1]]
    nodedepth = math.floor((1/2)*(math.sqrt(8*target-1)+1))
    #print('nodedepth:', nodedepth)
    remainder_of_target = target - depthscore(nodedepth)
    #print('remainder of target:', remainder_of_target)
    leftover_nodes = nodes - nodedepth
    #print('leftover_nodes:', leftover_nodes)

    # remainder of target is the new target

    backups = 0
    while (depthscore(leftover_nodes) < remainder_of_target) or (remainder_of_target < leftover_nodes):
        backups += 1
        print('cannot reach, backing up 1 node')
        nodedepth -= 1
        remainder_of_target = target - depthscore(nodedepth)
        print('remainder of target:', remainder_of_target)
        leftover_nodes = nodes - nodedepth
        print('leftover_nodes:', leftover_nodes)
        

    branch = nodes - leftover_nodes
    branchscore = depthscore(branch)
    if (abs(remainder_of_target-leftover_nodes) in [0, 1]):
        print('found that case')
        print('pretty sure I hit the last major branch with more than a depth of 1 or 2')
        print('branch score', branch)
        print('nodes in branch', branchscore)
        print('remainder of target:',remainder_of_target)
        print('leftover nodes:', leftover_nodes)
        data.append([branch, branchscore, leftover_nodes, remainder_of_target])
        return

    elif (depthscore(leftover_nodes) > remainder_of_target) and (remainder_of_target > leftover_nodes):
        print(f'reached score of {branchscore} using {branch} nodes with remainder of {remainder_of_target} and {leftover_nodes} left over nodes while backing up {backups} times') 
        data.append([branch, branchscore, leftover_nodes, remainder_of_target])
        findMaxdepth(leftover_nodes, remainder_of_target)

    else:
        print('unexpected')
    print('hi')
        


nodes = 7
goal = 8

nodes -= 1
findMaxdepth(nodes, goal)
print(data)

nodesused = 0
checkscore = 0
for each in data:
    nodesused += each[0]
    checkscore += each[1]
nodesused += data[-1][2]
checkscore += data[-1][3]

print('nodesused', nodesused)
print('checkscore', checkscore)


# build stupid 2-D array
array = []
marker = 2
for d in data:
    parent = 1
    for i in range(d[0]):
        array.append([parent, marker])
        parent += 1
        marker += 1
if data[-1][2] == data[-1][3]:
    array.extend([[1, marker+x] for x in range(data[-1][2])])
else:
    array.append([1, marker])
    p = marker
    marker+=1
    array.append([p, marker])
    marker+=1
    array.extend([[1, marker+x] for x in range(data[-1][2]-2)])

print(array)
print(len(array))




