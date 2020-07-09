from timeit import timeit


toSetup = '''
from collections import Counter
from string import ascii_lowercase, ascii_uppercase, ascii_letters
s = 'ajldjaklfjDASFGAEAG214u8312jfasdfjjajlejljjEATDAGCVdajej3nf9cjdeaGAGAHHDBJIEAWJISJBNT784456484823131848541658j3axcndkwoATYAHAcjeldjaklfjDASFGAEAG214u8312jfasdfjjajlejljjEATDAGCVdajej3nf9cjdeaGAGAHHDBJIEAWJISJBNT784456484823131848541ldjaklfjDASFGAEAG214u8312jfasdfjjajlejljjEATDAGCVdajej3nf9cjdeaGAGAHHDBJIEAldjaklfjDASFGAEAG214u8312jfasdfjjajlejljjEATDAGCVdajej3nf9cjdeaGAGAHHDBJIEAWJISJBNT784456484823131848541658j3axcndkwoATYAHAcjWJISJBNT784456484823131848541658j3axcndkwoATYAHAcj658j3axcndkwoATYAHAcj'*200
pat = ascii_letters+'13579'+'02468'
'''

toTest = '''
bundle = sorted(Counter(s).items(), key= lambda k: k)
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
'''

toTest2 = '''
d = {ch: 0 for ch in pat}
for i in s:
    d[i] += 1
res = ''
for k in d.keys():
    res += k*d[k]'''

toTest3 = '''
d = Counter([ch for ch in pat])
d.subtract(pat)
d.update(s)
res = ''
for k in d.keys():
    res += k*d[k]
'''

toTest4 = '''
def keyFunc(c: str):
    if c in ascii_lowercase:
        return ord(c)
    if c in ascii_uppercase:
        return ord(c) + 100
    if ord(c) % 2 == 1:
        return ord(c) + 200
    return ord(c) + 300

result = sorted(s, key=keyFunc)
res = ''
for i in result:
    res += i
'''

toTest5 = '''
def keyFunc(c: str):
    if c in ascii_lowercase:
        return ord(c)
    if c in ascii_uppercase:
        return ord(c) + 100
    if ord(c) % 2 == 1:
        return ord(c) + 200
    return ord(c) + 300

result = sorted(s, key=keyFunc)
a = ''.join(result)
'''

toTest6 = '''
a = f"{*s, key=lambda c: (-ord(c) >> 5, c in '02468', c)), sep='')}"
'''


print(timeit(toTest, setup= toSetup, number=1))
print(timeit(toTest2, setup= toSetup, number=1))
print(timeit(toTest3, setup= toSetup, number=1))

print(timeit(toTest4, setup= toSetup, number=1))
print(timeit(toTest5, setup= toSetup, number=1))
print(timeit(toTest6, setup= toSetup, number=1))


