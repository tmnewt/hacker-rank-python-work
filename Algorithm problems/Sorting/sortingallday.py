import os
import time


def quickSort(arr):
    pivot = arr[0]
    equal = []
    left = []
    right = []
    for i in arr:
        if i == pivot:
            equal.append(i)
        if i < pivot: 
            left.append(i)
        if i > pivot:
            right.append(i)
        
    return left + equal + right

def insertionSort(l):
    sort_counts = 0
    for i in range(1, len(l)):
        j = i-1
        key = l[i]
        while (j >= 0) and (l[j] > key):
            l[j+1] = l[j]
            j -= 1
            sort_counts += 1
        l[j+1] = key
        if i%100 == 0:
            print(f'at index {i} ')
        if sort_counts%1000 == 0:
            print(f'sorted indexes {sort_counts} times')
    return l

os.chdir('Algorithm problems\\Sorting\\tests')
fp = open('large_random_ints_unique', 'r')
arr = list(map(int, fp.read().rstrip().split()))

start_time = time.time()

#test insertionSort
#arr = quickSort(arr)
#insertionSort(arr)
#print('done')

arr.sort()

print(time.time() - start_time)




