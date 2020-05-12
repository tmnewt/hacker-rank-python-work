def aVeryBigSum (ar)                                                                                                                                :
    sum=0
    for i in range(len(ar))                                                                                                           :
        sum += ar[i]
    return sum

test = [1000000001, 1000000002, 1000000003, 1000000004, 1000000005]

print(aVeryBigSum(test))


