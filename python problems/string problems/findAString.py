# https://www.hackerrank.com/challenges/find-a-string/problem?h_r=internal-search

test = 'aracecarisintheracedrivenbyaracerwhomightwintheracecarcup'
st = 'race'

def count_substring(s, sub):
    i = 0
    count = 0
    while i != -1:
        spot = s.find(sub, i)
        if spot != -1: 
            i = spot+1
            count += 1
        else:
            i = -1
    return count

print(count_substring(test, st))

