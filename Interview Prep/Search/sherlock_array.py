# https://www.hackerrank.com/challenges/sherlock-and-array/problem

# answer this question. 
# Given an array can you select an element and split the 
#   array in 2 such the elements of the sub-arrays both 
#   sum to the same value? 

# elements may be zero, additionally if a sub-array 
#   contains no elements its value is 0.

# I think the trick here is to generate 2 running total arrays
#   one going from the front the other going from the back.
#   Then, compare these new running total arrays and look for 
#   values that equal each other in the same position.
def balancedSums(arr:list):
    sums_arr = [0]*len(arr)
    running_sum = 0
    for i, val in enumerate(arr):
        running_sum += val
        sums_arr[i] = running_sum
    
    running_sum = 0
    sums_barr = [0]*len(arr)
    for i, val in enumerate(reversed(arr)):
        running_sum += val
        sums_barr[i] = running_sum
    sums_barr.reverse()
    
    for p, q in zip(sums_arr, sums_barr):
        if p == q:
            return "YES"
    return "NO"


def balancedSumsPrintout(arr:list):
    sums_arr = [0]*len(arr)
    running_sum = 0
    for i, val in enumerate(arr):
        running_sum += val
        sums_arr[i] = running_sum

    running_sum = 0
    barr = reversed(arr)
    sums_barr = [0]*len(arr)
    for i, val in enumerate(barr):
        running_sum += val
        sums_barr[i] = running_sum
    sums_barr.reverse()
    evaluated_answer = "NO"
    for p, q in zip(sums_arr, sums_barr):
        if p == q:
            evaluated_answer = "YES"
            break
    if len(arr) <= 20:
        print('[', end='')
        for elem in sums_arr:
            print(f'{elem:6}, ', end='')
        print(']')
        print('[', end='')
        for elem in sums_barr:
            print(f'{elem:6}, ', end='')
        print(']')
    return evaluated_answer


tests = [
    ([1, 1, 4, 1, 1,0,0,0,0,0], 'YES'),
    ([1, 2, 4, 1, 1], 'NO'),
    ([1, 2, 4, 1, 1, 1], 'YES'),
    ([2, 0, 0, 0], 'YES'),
    ([0, 0, 0, 0,], 'YES'),
    ([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 9, 8, 7, 6, 15, 0, 0, 0 ,0 ,0, 0, 0, 0, 0, 0, 0], 'YES')
]

for i, data in enumerate(tests):
    test_data, answer = data
    print(f'Test {i}: Running Total array comparison')
    response = balancedSumsPrintout(test_data)
    print(f'Program Response: {response}.  Actual answer: {answer}\n')



