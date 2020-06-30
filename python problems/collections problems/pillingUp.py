# https://www.hackerrank.com/challenges/piling-up/problem

# reminds me of the tower of Hanoi game.
'''Constraints: 
Up to 5 test cases
1 <= n <= 100,000
1 <= sideLength <= 2,147,483,648

This problem is building out a list that is decreasing by size.
deque would be best at handling the starting cube row.
The naive solution would be to pick the larger of left or right. In fact,
is the naive solution robust? '''

#import timeit
from collections import deque


t = int(input())
for z in range(t):
    n = int(input())
    cubes = deque(list(map(int, input().split())))
    tower = deque()
    answer = 'Yes'

    # set up tower
    left = cubes[0]
    right = cubes[-1]
    if left >= right:
        tower.append(left)
        cubes.popleft()
    else:
        tower.append(right)
        cubes.pop()

    while True:
        # by default the answer is yes. iterate over to prove otherwise.
        #try will catch if cubes is empty. Break if IndexError
        try:
            left = cubes[0]
            right = cubes[-1]
            top = tower[-1]
            
            # catch if both right and left are greater than tower
            if left > top < right:
                answer = 'No'; break
            
            # by default if both equal top then pick left
            if left == top:
                tower.append(left)
                cubes.popleft()
            elif right == top:
                tower.append(right)
                cubes.pop()
            
            elif top > left > right:
                tower.append(left)
                cubes.popleft()
            
            elif top > right > left:
                tower.append(right)
                cubes.pop()

            elif top > left == right:
                tower.append(left)
                cubes.popleft()

            elif right > top > left:
                tower.append(left)
                cubes.popleft()
            
            elif left > top > right:
                tower.append(right)
                cubes.pop()
            
            
        except IndexError:
            break
    print(answer)

#testSetup = '''
#from collections import deque
#dumb = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]*1000000
#d = deque(dumb)'''
#
#

#
#print(timeit.timeit('''
#d[-1]
#''', setup= testSetup))
#
#print(timeit.timeit('''
#stor = d.pop()
#d.append(stor)
#''', setup= testSetup))
#
#print(timeit.timeit('''
#d[0]
#''', testSetup))
#
#print(timeit.timeit('''
#stor = d.popleft()
#d.appendleft(stor)
#''', setup='''
#from collections import deque
#d = deque([1,2,3,4,5,6,7,8,9,10,11,12,13,14])
#'''))

#        