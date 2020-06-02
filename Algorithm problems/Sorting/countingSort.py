
a_test = '63 25 73 1 98 73 56 84 86 57 16 83 8 25 81 56 9 53 98 67 99 12 83 89 80 91 39 86 76 85 74 39 25 90 59 10 94 32 44 3 89 30 27 79 46 96 27 32 18 21 92 69 81 40 40 34 68 78 24 87 42 69 23 41 78 22 6 90 99 89 50 30 20 1 43 3 70 95 33 46 44 9 69 48 33 60 65 16 82 67 61 32 21 79 75 75 13 87 70 33'
test = list(map(int, a_test.rstrip().split()))

def countingSort(arr):
    counts = [ 0 for _ in range(100)]
    for i in arr:
        counts[i] += 1
    return counts

#print(countingSort(test))

def countingSort2(arr):
    counts = [ 0 for _ in range(100)]
    for i in arr:
        counts[i] += 1
    outs = []
    for i in range(100):
        if counts[i] > 0:
            for _ in range(counts[i]):
                outs.append(i)
    return outs

#print(countingSort2(test))

# https://www.hackerrank.com/challenges/countingsort4/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

# the following countSort function should construct and print out the sorted strings.
# the first half of the strings should be converted to dashes.
# arr is 2D array where each arr[i] is comprised of 2 strings: x and s


test2 = [['0', 'ab'], [6,'cd'], [0, 'ef'], [6, 'gh'], [4, 'ij'], [0, 'ab'],
[6, 'cd'], [0, 'ef'], [6, 'gh'], [0, 'ij'], [4, 'that'], [3, 'be'],
[0, 'to'], [1, 'be'], [5, 'question'], [1, 'or'], [2, 'not'], [4, 'is'],
[2, 'to'], [4, 'the']]

def countSort(arr: list):
    outs = [[] for _ in range(len(arr))]
    for i in range(len(arr)):
        arr[i][0] = int(arr[i][0]) 
        if i < int(len(arr)/2):
            arr[i][1] = '-'
    for a in arr:
        outs[a[0]].append(a[1])
    return ' '.join(map(' '.join, outs)).strip()

print(countSort(test2))



