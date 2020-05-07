# left rotation
# a left rotation on an array of size n shifts each of the array's 
# elements 1 unit to the left.
# 

# should try this as though I had to no zero access 
# to better functionality

def leftrotation(ar: list, n: int):
    arr = ar
    for _ in range(n):
        arr.append(arr.pop(0))
    answer = ''
    for i in arr:
        answer = answer + str(i) + ' '
    return answer
eggs = [1,2,3,4,5]

print(leftrotation(eggs, 2))



test = ['Tim','Becca',3,2,1]
rotate = 3
expected_output = [2,1,'Tim','Becca',3]

def starLeftrotation(ar: list, n: int):
    store = None
    for _ in range(n):
        store = ar[0]
        for i in range(len(ar)):
            if i == (len(ar)-1):
                ar[i] = store
            else:
                ar[i] = ar[i+1]
    print(ar)
#starLeftrotation(test, 3)



# [1,2,4,8,16]
# store = 1
# when i = 0
# [2,2,4,8,16]
# when i = 1
# [2,4,4,8,16]
# when i = 2
# [2,4,8,8,16]
# when i = 3 
# [2,4,8,16,16]       
# when i = 4, trigger store
# [2,4,8,16,store]


#print(test)

#test.pop()
#print(test)



    