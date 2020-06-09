#https://www.hackerrank.com/challenges/find-the-median/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

def findMedian(arr: list):
    arr.sort()
    median_index = int((len(arr)+1)/2)-1
    return arr[median_index]

test = [1, 3, 4, 2, 5, 6, 10]

test.sort()
print(test)
print(findMedian(test))