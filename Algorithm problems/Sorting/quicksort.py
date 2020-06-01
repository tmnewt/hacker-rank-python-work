# https://www.hackerrank.com/challenges/quicksort1/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

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

test = [5, 3,2, 1, 7, 9, 34, 10, 4, 4, 2]

print(quickSort(test))