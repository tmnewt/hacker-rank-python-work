from string import ascii_lowercase, ascii_uppercase

s = 'ajldjaklfjDASFGAEAG214u8312jfasdfjjajlejljjEATDAGCVdajej3nf9cjdeaGAGAHHDBJIEAWJISJBNT784456484823131848541658j3axcndkwoATYAHAcjeldjaklfjDASFGAEAG214u8312jfasdfjjajlejljjEATDAGCVdajej3nf9cjdeaGAGAHHDBJIEAWJISJBNT784456484823131848541ldjaklfjDASFGAEAG214u8312jfasdfjjajlejljjEATDAGCVdajej3nf9cjdeaGAGAHHDBJIEAldjaklfjDASFGAEAG214u8312jfasdfjjajlejljjEATDAGCVdajej3nf9cjdeaGAGAHHDBJIEAWJISJBNT784456484823131848541658j3axcndkwoATYAHAcjWJISJBNT784456484823131848541658j3axcndkwoATYAHAcj658j3axcndkwoATYAHAcj'*200

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


