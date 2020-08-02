import os
import numpy as np
#from collections import deque

#def performOperations(N, op):
#    arr = deque([x+1 for x in range(N)])
#    answer = []
#    for p in op:
#        #print('p = ', p)
#        if p in arr:
#        #    print('swap')
#            if len(arr) == 1:
#                pass
#            elif len(arr) == 2:
#                arr.rotate(1)
#            else:
#        #        print(arr)
#                to_the_back = arr.popleft()
#                to_the_front = arr.pop()
#                arr.append(to_the_back)
#                arr.appendleft(to_the_front)
#        #        print(arr)
#        else:
#        #    print('replace end')
#            try:
#        #        print(arr)
#                arr.pop()
#            except IndexError:
#                pass
#        #    print(arr)
#            arr.append(p)
#        #    print(arr)
#        #print(sum(arr))
#        print(sum(arr))
#            
    



#moves =  np.random.randint(1, 30000000, 200000)

#moves = [4, 2]

#result = performOperations(3, moves)
#print('\n'.join(map(str, result)))
#print('done')


def performOperations(N, op):
    score = (N*(N+1))//2
    front = 1
    end = N 
    answers = []

    for p in op:
        if (p == front) or (p == end) or (2 <= p <= N-1):
            store = front
            front = end
            end = store
        else:
            score += (p - end)
            end = p
        answers.append(score)
    return answers

#if __name__ == '__main__':
#    fptr = open(os.environ['OUTPUT_PATH'], 'w')
#    #test = open('testme', 'w')
#
#    N, M = list(map(int, input().split()))
#    op = [int(input()) for _ in range(M)]
#
#    result = performOperations(N, op)
#
#    
#    #print('\n'.join(map(str, result)))
#
#    #test.write('\n'.join(map(str, result)))    
#    #test.close()
#    #fptr.write('\n'.join(map(str, result)))
#    #fptr.write('\n')
#    fptr.close()


print(performOperations(3, [4,1000]))

        


