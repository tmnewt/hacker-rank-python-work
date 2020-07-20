# https://www.hackerrank.com/challenges/matrix-script/problem

# absolutely no if statements are allowed.

import string
import random
import re

expr = re.compile(r'(?<=\w)[!@#$% &]{1,}(?=\w)')

random.seed(1)
allowedcharacters = string.ascii_letters + string.digits + '!@#$% &' # len is 69.


def makeMatrix(multiStr: str):
    lines = multiStr.splitlines()
    return ''.join(lines)


def weightsgen(alphaNumericWeight: int, otherCharacterWeight: int):
    weights = []
    for _ in range(62):
        weights.append(alphaNumericWeight)
    for _ in range(7):
        weights.append(otherCharacterWeight)
    return weights

def generateMultiStr(length: int, height: int, alphaNumericWeight: int = 1, otherCharacterWeight = 3):
    multilist = []
    for _ in range(height):
        multilist.append(''.join(random.choices(
            population = allowedcharacters, 
            weights = weightsgen(alphaNumericWeight, otherCharacterWeight),
            k = length))+'\n')
    return ''.join(multilist)

print('start of crude random matrix\n')
matrixScript = generateMultiStr(40, 20)
print(matrixScript)
#matrix = makeMatrix(matrixScript)
#print(matrix)

#print('\n\nresults of regex operation\n')


# ==================
#   Part 1 complete
# ==================

# Finished the regex code and also built a random matrix script generator to test it on.
# Now to build a converter. Should be pretty straight forward using a zip function.

lines = matrixScript.splitlines()
ziplines = list(zip(*lines))
#print(ziplines)
matrixlist = []
for line in ziplines:
    matrixlist.append(''.join(line))
matrix = ''.join(matrixlist)
print(matrix)
new = re.sub(expr, ' ', matrix)
print('\n')
print(new)
