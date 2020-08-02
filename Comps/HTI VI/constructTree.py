import math
import os
import random
import re
import sys
import time

#
# Complete the 'treeConstruction' function below.
#
# The function is expected to return a 2D_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER N
#  2. LONG_INTEGER X
#
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


t = [12, 45, 3]
t.index(max(t))


def treeConstruction(N, X):
    if (N-2 >= X) or (X > ((N*(N-1))/2)):
        return [[-1, -1]]
    else:
        upp, low, last= findOptBranches(N, X)
        box = flatbox(N, upp)
        print(box)
        score = scores(box)
        decycle = 1
        toppicked = True
        while score != X:
            length = len(box)
            bottom = box.index(min(box))
            print(sum(box))
            print(score)
            if box[bottom] <= 0:
                box.pop(bottom)
                continue
            if score > X:
                if toppicked:
                    top = box.index(max(box))
                    box[top] = box[top] -1
                    box[bottom] = box[bottom] +1
                    toppicked = not toppicked
                else:    
                    box[decycle] = box[decycle] - 1
                    box[bottom] = box[bottom] + 1
                    decycle += 1
                    score = scores(box)
                    toppicked = not toppicked

            elif score < X:
                box[0] = box[0] + 1
                box[bottom] = box[bottom] -1
                score = scores(box)

            if decycle == length-1:
                decycle = 1
            print(box)
        print(score)
            

                 

        #while score != X:
        #    print(score)
        #    if score > X:
        #        box[-1] = box[-1] + 1
        #        box[decycle] = box[decycle] - 1
        #        decycle += 1
        #        score = scores(box)
        #
        #    elif score < X:
        #        box[0] = box[0] + 1
        #        box[-1] = box[-1] - 1
        #        score = scores(box)
#
        #    if decycle == length-1:
        #        decycle = 1
        #    print(box)
        #    time.sleep(0.05)
        #print(score)
            


treeConstruction(932, 59999)


#prior = depthscore(104)+depthscore(50)
#for i in range(1,50):
#    snext = depthscore(104-i)+depthscore(50+i)
#    print(prior)
#    print(snext-prior)
#    prior = snext

#ah = depthscore(104)
#be = depthscore(100)
#print(ah-be)
#kill = depthscore(105)
#me = depthscore(99)
#print(kill-me)
#
#print((ah+be)-(kill+me))
#
#fuck = depthscore(103)
#you = depthscore(101)
#
#print((ah+be)-(fuck+you))
#
#Iwant = depthscore(102)
#todie = depthscore(102)
#
#print((fuck+you)-(Iwant+todie))
        



        
#if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')
#
#    T = int(input().strip())
#
#    for T_itr in range(T):
#        first_multiple_input = input().rstrip().split()
#
#        N = int(first_multiple_input[0])
#
#        X = int(first_multiple_input[1])
#
#        result = treeConstruction(N, X)
#
#        fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
#        fptr.write('\n')
#
#    fptr.close()


#nodes = 958
#test = 2568565
#findOptBranches(nodes, test)
#print(flatbox(nodes, 17))






def oldflatten(a, b):
    remainder = a%b
    print(remainder)
    if remainder == 0:
        tmp = []
        peak = a//b
        score = b*depthscore(peak)
        for i in range(b):
            tmp.append(a//b)
    else:
        diff = b-remainder
        peak = (a+diff)//b
        tmp = []
        for i in range(b):
            tmp.append((a+diff)//b)
        score = (b-1)*depthscore(peak)+depthscore(peak-diff)    
        tmp[-1] = tmp[-1]-diff
    print(tmp)
    print(score)
    unpackscore = 0
    for i in tmp:
        unpackscore += depthscore(i)
    print(unpackscore)


            






    





