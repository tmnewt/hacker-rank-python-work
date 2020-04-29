# https://www.hackerrank.com/challenges/determining-dna-health/problem

# do I want to use dictionary or tuples? 
# eh, lets go with Tuples...

import re
import sys
import platform


#test_dna = ['caaab']
#test_genes = ['a', 'b', 'c', 'aa', 'd', 'b']
#test_health = [1, 2, 3, 4, 5, 6]

#package = list(tuple(zip(test_genes, test_health)))
#print(package)
#print(package[1])
#print(package[1][1])
#
## grab d, 5
#print(package[4])
#
#print(package[1:5])
#print(type(package))
#print(list(package))

#print(re.findall('a(?=a)', 'aaa'))


# given test_dna (see above)
# given gene pool (see above) set of 1 to 5 indexed at zero
# given each gene in genepool has an associated health value (see above)
# given that a gene in the pool can reoccur with multiple values (see above)
# retrieve the sum of the health of the dna string
#           What about minimums?
# find max health and min health of the dna string.
#


# walkthrough of string 'caaab' with first 1 and last 5
#
#
# recall gene_pool is ['a', 'b', 'c', 'aa', 'd', 'b'] 
#               ignore 0 index because it falls outside of range of 1 to 5 (inclusive btw)
#               applicable gene_pool is technically ['b', 'c', 'aa', 'd', 'b']  <-- use this
#
# recall each gene has an associated value (easy to tie those to a sub string using tuple (see earlier))
#               ignore 0 index because it falls outside of range of 1 to 5 (inclusive btw)
#               applicable gene_pool health is:     [2, 3, 4, 5, 6]  
# 
# Assume everything was already zipped together as a tuple so the applicable values are as follows:
# 
#               (('b', 2), ('c', 3), ('aa', 4), ('d', 5), ('b', 6))
#
# ^^^ This is what is applicable. ^^^ But subsets like this doesn't necessarily need to be stored in memory
# 
# Now evaluate the DNA string:
#           recall DNA string is 'caaab'
#           
#           start by looking at 0 index of the DNA string
#                   are there any substrings from index 0 to end  that  are found in the applicable gene pool?
#                       yes
#                       the substring 'c' can be found in the DNA string. 
#                   but we need to keep asking that question for all substrings starting at index 0:
#                       is 'ca' in the gene pool?   No.  Ignore it.
#                       is 'caa' in the gene pool?   No.  Ignore it.
#                       is 'caaa' in the gene pool?   No.  Ignore it.
#                       is 'caaab' in the gene pool?   No.  Ignore it.
#                   That is essentially what we are considering. Now with regular expressions we essentially don't have to worry about them
#                   Now we are done with index 0 of the DNA string
#           
#           now look at 1 index of DNA string
#                   are there any substrings from index 1 to end that are found in the applicable gene pool?
#                       yes
#                       the substring 'aa'
#                   there is also the following implied questions
#                       is 'a' in the gene pool?  Yes but it's not in the applicable gene pool. So, no.  Ignore it.
#                       is 'aaa' in the applicable gene pool? No, ignore it.
#                       is 'aaab' in the applicable gene pool? No, ignore it.
#                   
#           rinse and repeat until you get to the last index of the dna string:
#                    are there any substrings in the last index that are found in the applicable gene pool?
#                       yes. There are 2.  b and b 
#                       those are distinct and they both are in the applicable gene set. 
#                       the fact that their value collide can be ignored. So double count them!
# 
#          
# 

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



test_dna = 'caaab'
test_dna2 = 'caaabbccaaaa'
test_genes = ['a', 'b', 'c', 'aa', 'd', 'b']
test_health = [1, 2, 3, 4, 5, 6]

pool = describe_gene_pool(test_genes, test_health)
print(healthDNA(pool, 1, 5, test_dna2))  # later test dna 'caaabbccaaaaab'
print('done\n')

# caaabbccaaaa should return the following values
# c = 3         3
# aa = 4        7  
# aa = 4        11
# b = 2         13
# b = 6         19
# b = 2         21
# b = 6         27
# c = 3         30
# c = 3         33
# aa = 4        37
# aa = 4        41
# aa = 4        45
    



# x = re.compile('a')
# matches = re.findall(x, 'caaab')
# print(len(matches))
# print(x.pattern)



