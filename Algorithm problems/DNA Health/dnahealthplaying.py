# https://www.hackerrank.com/challenges/determining-dna-health/problem

# do I want to use dictionary or tuples? 
# eh, lets go with Tuples...

import re

test_genes = ['a', 'b', 'c', 'aa', 'd', 'b']
test_health = [1, 2, 3, 4, 5, 6]

package = tuple(zip(test_genes, test_health))
print(package)
print(package[0][1])  # << that's going to get annoying




