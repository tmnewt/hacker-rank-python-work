arr=[1, 1, 0, -1, -1, 5, 6]
def plusMinus(arr):
    acount=0
    bcount=0
    ccount=0
    for i in arr:
        if i>0:
            acount += 1
        if i==0:
            bcount += 1
        if i<0:
            ccount += 1
    afinal = (acount/len(arr))
    cfinal = (ccount / len(arr))
    bfinal = (bcount / len(arr))

    print(format(afinal, '.6f'))
    print(format(cfinal, '.6f'))
    print(format(bfinal, '.6f'))

plusMinus(arr)