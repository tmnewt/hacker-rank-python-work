#!/bin/python3
import re

def describe_gene_pool(genes, health):
    return list(tuple(zip(genes, health)))

def healthDNA(gene_pool, start, end, dna):
    total_health = 0
    for i in range(start, end+1):
        gene = gene_pool[i][0]
        x = None
        if len(gene) > 1:
            x = re.compile(f'{gene[0]}(?={gene[1:]})')
        else:
            x = re.compile(f'{gene}')
        matches = len(re.findall(x, dna))
        total_health += matches*gene_pool[i][1]
    return total_health

if __name__ == '__main__':
    n = int(input())

    genes = input().rstrip().split()

    health = list(map(int, input().rstrip().split()))
    
    pool = describe_gene_pool(genes, health)

    s = int(input())

    minimum = None
    maximum = 0

    for s_itr in range(s):
        firstLastd = input().split()

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
    
    print(f'{minimum} {maximum}') 

        
