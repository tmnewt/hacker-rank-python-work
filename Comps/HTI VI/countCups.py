import os


def countCups(n, balls, swaps, queries):
    arr = [0]*n
    for b in balls:
        arr[b-1] = 1
        print(arr)

    for swap in swaps:
        print(arr)
        p, q = swap
        v = arr[p-1]
        w = arr[q-1]
        print(p)
        print(q)
        if v == w:
            pass
        else:
            s = v
            arr[p-1] = arr[q-1]
            arr[q-1] = s
        print(arr)

    running_sum = 0
    i = 0
    end = len(arr)
    while i < end:
        arr[i] = running_sum + arr[i]
        running_sum = arr[i]
        i+=1
        print(arr)

    answers = []
    for i in queries:
        p, q = i
        v = arr[p-1]
        w = arr[q-1]

        if p == 1:
            answers.append(w)
        else:
            r = arr[p-2]
            if r != v:
                answers.append(1+w-v)
            else:
                answers.append(w-v)
    
    return answers
    





if __name__ == '__main__':

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    s = int(first_multiple_input[2])

    q = int(first_multiple_input[3])

    balls = list(map(int, input().rstrip().split()))

    swaps = []

    for _ in range(s):
        swaps.append(list(map(int, input().rstrip().split())))

    query = []

    for _ in range(q):
        query.append(list(map(int, input().rstrip().split())))

    result = countCups(n, balls, swaps, query)

    #fptr.write(' '.join(map(str, result)))
    #fptr.write('\n')

    #fptr.close()