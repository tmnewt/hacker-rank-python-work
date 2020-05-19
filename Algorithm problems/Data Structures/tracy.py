def arrayManipulation(n: int, queries: list):
    arr = [0 for _ in range(n+2)]
    for query in queries:
        
        a = query[0]
        b = query[1]
        k = query[2]

        arr[a] += k
        arr[b+1] -= k

    max_prefix_sum = 0
    prefix_sum = 0
    for i in arr:
        prefix_sum += i
        if prefix_sum > max_prefix_sum:
            max_prefix_sum = prefix_sum

    return max_prefix_sum
    