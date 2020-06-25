# https://www.hackerrank.com/challenges/balanced-brackets/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=stacks-queues

import os

def isBalanced(s: str):
    stack = []
    balanced = 'YES'
    for i in s:
        # stack
        if i == '(': stack.append(i)
        if i == '[': stack.append(i)
        if i == '{': stack.append(i)

        if (i == ')'):
            try: 
                if '(' != stack.pop():
                    balanced = 'NO'
                    break
            except:
                balanced = 'NO'
                break
        if (i == ']'):
            try: 
                if '[' != stack.pop():
                    balanced = 'NO'
                    break
            except:
                balanced = 'NO'
                break
        if (i == '}'):
            try: 
                if '{' != stack.pop():
                    balanced = 'NO'
                    break
            except:
                balanced = 'NO'
                break
    if len(stack) != 0:
        balanced = 'NO'
    return balanced

#os.chdir('Interview Prep\\Stacks and Queues')
#fp = open('balancetest', 'r')
#lines = fp.readlines()
#fp.close
#
#for i in range(1, len(lines)):
#    print(f'{i}: {isBalanced(lines[i])}')

# number 16
print(isBalanced('{{}('))