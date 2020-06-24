# https://www.hackerrank.com/challenges/polar-coordinates/problem

from cmath import phase
from math import sqrt

def polarCoordinate(s: str):
    z = complex(s)
    x = float(z.real)
    y = float(z.imag)

    print(sqrt(x**2 + y**2))
    print(phase(z))

polarCoordinate(input())

#s = complex(input())
#print(s.real)
#print(s.imag)

