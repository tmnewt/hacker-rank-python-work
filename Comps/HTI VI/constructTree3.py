
import math

def depthscore(n):
    return ((n+1)*n)//2


def treeConstruction(nodes, target):
    if (nodes - target >= 2) or (target > ((nodes*(nodes-1))/2)) or ((nodes==4 and target==5)):
        #print('throw out')
        return [[-1, -1]]
    data = []
    def findMaxdepth(nodes, target):
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
            #print('cannot reach, backing up 1 node')
            nodedepth -= 1
            remainder_of_target = target - depthscore(nodedepth)
            #print('remainder of target:', remainder_of_target)
            leftover_nodes = nodes - nodedepth
            #print('leftover_nodes:', leftover_nodes)


        branch = nodes - leftover_nodes
        branchscore = depthscore(branch)
        if (abs(remainder_of_target-leftover_nodes) in [0, 1]):
            #print('found that case')
            #print('pretty sure I hit the last major branch with more than a depth of 1 or 2')
            #print('branch score', branchscore)
            #print('nodes in branch', branch)
            #print('remainder of target:',remainder_of_target)
            #print('leftover nodes:', leftover_nodes)
            data.append([branch, branchscore, leftover_nodes, remainder_of_target])
            return

        elif (depthscore(leftover_nodes) > remainder_of_target) and (remainder_of_target > leftover_nodes):
            #print(f'reached score of {branchscore} using {branch} nodes with remainder of {remainder_of_target} and {leftover_nodes} left over nodes while backing up {backups} times') 
            data.append([branch, branchscore, leftover_nodes, remainder_of_target])
            findMaxdepth(leftover_nodes, remainder_of_target)

        else:
            print('unexpected')

    nodes-=1   
    findMaxdepth(nodes, target)
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
    return array

answer = treeConstruction(3000,999999)
print(len(answer))
print(answer)

#for i in range(100):
#    print(treeConstruction(5+i, 6+i))


from collections import Counter

def findedge(l:list):
    secondNode = []
    for each in l:
        secondNode.append(each[1])

    print(Counter(secondNode))
    Counter()

findedge(answer)
    