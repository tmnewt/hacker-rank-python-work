import os

nothing ='''
Starting with a 1-indexed array of zeros and a list of operations, 
for each operation add a value to each of the array element between 
two given indices, inclusive. Once all operations have been performed, 
return the maximum value in your array. 
'''
# for example given the length of your array of zeros n = 10 indexed at 1
# we have [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# then, given inputs such as,
#       [1, 5, 3] parse this as  a = 1, b = 5,  k = 3
#           where a and b describes the range of indexes (inclusive) to operate on.
#       
#       the only operation is to add k.
# 
#       after this line of inputs the array would look like:
#       [3, 3, 3, 3, 3, 0, 0, 0, 0, 0]
# # 


def arrayManipulation(n: int, queries: list):
    arr = [0 for _ in range(n)]
    count = 0
    for query in queries:
        
        a = query[0]-1 #overwrite 1-indexing constraint to 0 index... because I can!
        b = query[1]-1 #overwrite 1-indexing constraint to 0 index... because I can!
        k = query[2]  # the value to use in operation

        spam = [k for _ in range(b-a+1)]

        arr[a:b+1] = [sum(x) for x in zip(arr[a:b+1], spam)]
        count += 1 
        if count%10 == 0:
            print(f'completed {count}')
        
    return max(arr)



#print(arrayManipulation(size, test_queries))

def arrayManipulation_Tracey(n: int, queries: list):
    arr = [0 for _ in range(n)]
    count = 0
    for query in queries:

        a = query[0]-1
        b = query[1]-1
        k = query[2]

        while (a <= b):
            arr[a] += k
            a += 1
        
    return max(arr)





#print(arrayManipulation(test1_n, test1_query))

# test7 answer is 2497169732
# test9 answer is 2501448788

#print(arrayManipulation_Tracey(test1_n, test1_query))

def arrayManipulation_Sum_Prefix(n: int, queries: list):
    arr = [0 for _ in range(n+1)]
    for query in queries:
        a = query[0]-1
        b = query[1]
        k = query[2]
        arr[a] += k
        arr[b] = arr[b]-k
    
    answer = prefixSum(arr)
    return answer

def prefixSum(arr):
    running_sum = 0
    for i in range(len(arr)):
        arr[i] = running_sum + arr[i]
        running_sum = arr[i]
        
    
    return max(arr)

os.chdir('Algorithm problems\\Data Structures')
fp = open('arraymaniptest9.txt', 'r')
lines = fp.readlines()
fp.close

startline = lines[0].rstrip().split()
size = int(startline[0])
runs = int(startline[1])

test_queries = []

for s_itr in range(runs):
    test_queries.append(list(map(int, lines[s_itr+1].rstrip().split())))


test1_n = 10
test1_query = [[1, 5, 3], [4, 8, 7], [6, 9, 1]]
answer = 10
print(arrayManipulation_Sum_Prefix(test1_n, test1_query))

test2_n = 5
test2_queries = [[2,3,603],[1,1,286],[4,4,882]]

print(arrayManipulation_Sum_Prefix(test2_n, test2_queries))

print(arrayManipulation_Sum_Prefix(size, test_queries))

test3_n = 5
test3_queries = [[1,2,100], [2,5, 100], [3,4,100]]



print(arrayManipulation_Sum_Prefix(test3_n, test3_queries))
print(arrayManipulation_Sum_Prefix(5, [[4,5,1]]))
print(arrayManipulation_Sum_Prefix(5, [[1, 2, 2], [2, 5, 2]]))