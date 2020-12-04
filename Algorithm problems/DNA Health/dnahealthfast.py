# convert large text files into input data.

import os
import re

def describe_gene_pool(genes, health):
    return list(tuple(zip(genes, health)))

def healthDNA(gene_pool, start, end, dna):
    total_health = 0
    for i in range(start, end+1):
        gene = gene_pool[i][0]
        x = None
        if len(gene) > 1:
            x = re.compile(gene[0]+"(?="+gene[1:]+')')
        else:
            x = re.compile(gene)
        matches = len(re.findall(x, dna))
        total_health += matches*gene_pool[i][1]
    return total_health

os.chdir('Algorithm problems\\DNA Health')
fp = open('test10.txt', 'r')
lines = fp.readlines()
fp.close

genes = lines[1].rstrip().split()

health = list(map(int, lines[2].rstrip().split()))

pool = list(tuple(zip(genes, health)))

s = int(lines[3])

minimum = None
maximum = 0

for s_itr in range(s):
    firstLastd = lines[4+s_itr].split()

    first = int(firstLastd[0])

    last = int(firstLastd[1])

    d = firstLastd[2]
    result = healthDNA(pool, first, last, d)
    if minimum == None:
        minimum = result
    if result < minimum:
        minimum = result
    if result > maximum:
        maximum = result
    if s_itr%100 == 0:
        print(f'finished: {s_itr}')
print(f'{minimum}, {maximum}')




#   gene pool: [abcd, a, ab, ac, ad, bc, cd, a, bb, bcd, abcd, aaaa, aa, a, aab, aba]
#   health   : [ 11,  3, 4,  5,  1,  20,  0, 6, 13,  15,  56,   99,  38, 45, 1,   8 ]
# setup check: [ x    x  x   x   x   x       x   x   x    x     x     x  x   x    x ]
