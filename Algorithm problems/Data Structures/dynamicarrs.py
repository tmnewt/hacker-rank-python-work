# Dynamic Arrays (not dy nami carrs...)
spam = '''Create a list, seqList, of N empty sequences, where each sequence is indexed from 0 to N-1. 
The elements within each of the sequences also use 0-indexing.

Create an integer, lastAnswer, and initialize it to 0.
The 2 types of queries that can be performed on your list of sequences (seqList) are described below:

Both queries are in the format of q x y where q is either 1 or 2, x is an int and y is an 

When First type of Query: 1 x y 
        1. Find the sequence, seq, at index ((x ^ lastAnswer)%N) in seqList.
        2. Append integer y to sequence seq.

When second type of Query: 2 x y
    Do this:
        1. Find the sequence, seq, at index ((x ^ lastAnswer)%N) in seqList.
        2. Find the value of element y(mod)size_of_seq and assign it to lastAnswer.
        3. Print the new value of lastAnswer on a new line

Given all this, display the output for some Q amount of queries
'''

q =[[1,0,5],
    [1,1,7],
    [1,0,3],
    [2,1,0],
    [2,1,1]]


def dynamicArray(n, queries):
    seqList = [[] for i in range(n)]
    lastAnswer = 0
    respones = []

    for query in queries:
        query_type = query[0]
        x = query[1]
        y = query[2]
        if query_type == 1:
            to_find = ((x^lastAnswer)%n)
            seqList[to_find].append(y)

        if query_type == 2:
            to_find = ((x^lastAnswer)%n)
            lastAnswer = seqList[to_find][y%len(seqList[to_find])]
            respones.append(lastAnswer)

    return respones


test_n = 100000
q = [[1, 301640676, 258929543],
[1, 797018914, 641381259],
[1, 662510471, 110776402],
[1, 927448644, 986028360],
[1, 425928921, 817358374],
[1, 673794026, 567902929],
[1, 652516820, 798692158],
[1, 29589106, 235382085],
[1, 88627543, 795421339],
[1, 232517350, 291842488],
[1, 768194707, 376754785]]


def dynamicArrayLookIn(n, queries):
    seqList = [[] for i in range(n)]
    lastAnswer = 0
    respones = []
    print(respones)

    for query in queries:
        query_type = query[0]
        x = query[1]
        y = query[2]
        if query_type == 1:
            print('query type 1')
            to_find = ((x^lastAnswer)%n)
            seqList[to_find].append(y)
            print(f'appending {y} to sublist {to_find}')

        if query_type == 2:
            to_find = ((x^lastAnswer)%n)
            lastAnswer = seqList[to_find][y%len(seqList[to_find])]
            respones.append(lastAnswer)

    return respones

dynamicArrayLookIn(test_n, q)


def xor_experiment(n: int):
    for i in range(n+1):
        for j in range(n+1):
            evaluation = i^j

            print(f'xor operation ({i}^{j}) output: {evaluation} because: {bin(i)} XOR {bin(j)} = {bin(evaluation)} the binary for {evaluation}')

#xor_experiment(10)

#a = 'Hello everyone'
#print(a[0:4:2])
#
#print(a[0:4][0])
#print(a[0:4][2])
#
#arr = ['Xi', 'Star', 'Locke', 'EE', 'Rat', 'Von', 'Skelly']
#
#print(arr[0:])
#print(arr[0::3])
#
#print(arr[2::2])
#

#a = 'Hello world'
#print(a[3:7:1])