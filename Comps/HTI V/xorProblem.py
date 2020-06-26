def maxXorValue(x: str, k):
    opp_max = ''
    count = 0
    i = 0
    while (count < k) and (i < len(x)):
        if x[i] == '0':
            opp_max = opp_max + '1'
            count += 1
        else:
            opp_max = opp_max + '0'
        i += 1
    return opp_max + '0'*(len(x)-i)

print(maxXorValue('10010', 5))
print(maxXorValue('10000000', 3))