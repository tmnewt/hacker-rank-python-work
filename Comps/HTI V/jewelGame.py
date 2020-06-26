# there is no way to play suboptimally

def getMaxScore(jewels: str):
    stack = []
    count = 0
    stack.append(jewels[0])
    for i in jewels[1:]:
        #print(stack)
        try:
            if i == stack[-1]: 
                stack.pop()
                count += 1
            else: stack.append(i)
        except:
            stack.append(i)
    return count 

print(getMaxScore('abcd'))



