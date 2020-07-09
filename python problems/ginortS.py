# https://www.hackerrank.com/challenges/ginorts/problem?h_r=next-challenge&h_v=zen

from string import ascii_lowercase, ascii_uppercase, ascii_letters
from collections import Counter
from timeit import timeit

s = 'ajldjaklfjDASFGAEAG214u8312jfasdfjjajlejljjEATDAGCVdajej3nf9cjdeaGAGAHHDBJIEAWJISJBNT784456484823131848541658j3axcndkwoATYAHAcjeldjaklfjDASFGAEAG214u8312jfasdfjjajlejljjEATDAGCVdajej3nf9cjdeaGAGAHHDBJIEAWJISJBNT784456484823131848541ldjaklfjDASFGAEAG214u8312jfasdfjjajlejljjEATDAGCVdajej3nf9cjdeaGAGAHHDBJIEAldjaklfjDASFGAEAG214u8312jfasdfjjajlejljjEATDAGCVdajej3nf9cjdeaGAGAHHDBJIEAWJISJBNT784456484823131848541658j3axcndkwoATYAHAcjWJISJBNT784456484823131848541658j3axcndkwoATYAHAcj658j3axcndkwoATYAHAcj'

bundle = Counter(s)
bundle = sorted(bundle.items(), key= lambda k: k)
lowers = []; uppers = []; odds = []; evens = []; i = 0; length = len(s)
for i in bundle:
    if i[0] in ascii_lowercase: lowers.append(i)
    if i[0] in ascii_uppercase: uppers.append(i)
    if i[0] in '13579': odds.append(i)
    if i[0] in '02468': evens.append(i)

res = ''
for l in lowers: res += l[0]*l[1]
for u in uppers: res += u[0]*u[1]
for o in odds:   res += o[0]*o[1]
for e in evens:  res += e[0]*e[1]
#print(res)



# some other stuff to ignore...
pat = ascii_letters+'13579'+'02468'
blob = Counter([ch for ch in pat])
blob.subtract(pat)
blob.update(s)





