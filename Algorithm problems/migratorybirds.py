# https://www.hackerrank.com/challenges/migratory-birds/problem?h_r=internal-search


import timeit
import numpy as np

np.random.seed(1)
nums = list(np.random.randint(1,6, size = 20000))


test1 = [8,4,4,5,3]
test2 = [2,5,5,3,1,1,1,10,10,10,4,4,5,5,4,4,4,2,1,1,33]
def migratoryBirds(arr: list):
    arr_set = list(set(arr))
    count_of_smallest_frequent = arr.count(arr_set[0])
    smallest_frequent_type = arr_set[0]
    for i in range(len(arr_set)):
        if (arr.count(arr_set[i]) == count_of_smallest_frequent) and (arr_set[i] < smallest_frequent_type):
            smallest_frequent_type = arr_set[i]

        if arr.count(arr_set[i]) > count_of_smallest_frequent:
            smallest_frequent_type = arr_set[i]
            count_of_smallest_frequent = arr.count(arr_set[i])
    
    return smallest_frequent_type

print(migratoryBirds(nums))

runs = 10000

print(timeit.timeit(f'''test2 = {nums}
def migratoryBirds(arr: list):
    arr_set = list(set(arr))
    count_of_smallest_frequent = arr.count(arr_set[0])
    smallest_frequent_type = arr_set[0]
    for i in range(len(arr_set)):
        if (arr.count(arr_set[i]) == count_of_smallest_frequent) and (arr_set[i] < smallest_frequent_type):
            smallest_frequent_type = arr_set[i]

        if arr.count(arr_set[i]) > count_of_smallest_frequent:
            smallest_frequent_type = arr_set[i]
            count_of_smallest_frequent = arr.count(arr_set[i])
    
    return smallest_frequent_type

migratoryBirds(test2)''', number=runs))



# test for faster script.

script = f'''test2 = {nums}
def migratoryBirds(arr: list):
    arr_set = list(set(arr))
    count_of_smallest_frequent = arr.count(arr_set[0])
    smallest_frequent_type = arr_set[0]
    for i in range(len(arr_set)):
        current = arr.count(arr_set[i])
        if (current == count_of_smallest_frequent) and (arr_set[i] < smallest_frequent_type):
            smallest_frequent_type = arr_set[i]

        if current > count_of_smallest_frequent:
            smallest_frequent_type = arr_set[i]
            count_of_smallest_frequent = arr.count(arr_set[i])
    
    return smallest_frequent_type

migratoryBirds(test2)'''

print(timeit.timeit(script, number=runs))

