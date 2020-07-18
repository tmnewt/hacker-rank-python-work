# https://www.hackerrank.com/challenges/reduce-function/problem?h_r=next-challenge&h_v=zen

from fractions import Fraction
from functools import reduce

# read the fractions module documentation here: https://docs.python.org/3/library/fractions.html
# read the functools module documentation here: https://docs.python.org/3/library/functools.html?highlight=reduce#functools.reduce

#a = Fraction(3,8)
#b = Fraction(1,2)
#c = a*b
#print(c.numerator, c.denominator)

def product(fracs):
    t = reduce((lambda x, y: Fraction(x.numerator * y.numerator, x.denominator * y.denominator)), fracs)
    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)


# turns out it is entirely possible to do the following 
#
#      reduce((lambda x, y: x*y), fracs)
#
# this is because fracs is already a list of Fraction objects.
# Fraction objects can be multiplied together in the same manner
# as one would on a piece of paper. Also python automatically simplifies them for our convienance.