# https://www.hackerrank.com/challenges/find-angle/problem

import math

#print(f'{math.cos(math.radians(90)):2f}')

ab = 1   #int(input())
bc = 100   #int(input())

hyp = math.sqrt(ab**2 + bc**2)
print(hyp)
hypMid = hyp/2
print(hypMid)
angleAB = math.asin(ab/hyp)
angleABdeg = math.degrees(angleAB)
print(angleABdeg)
angleBCdeg = 180 - 90 - angleABdeg
print(angleBCdeg)

bm = math.sqrt(hypMid**2 + bc**2 - 2*hypMid*bc * math.cos(angleAB))
print(bm)
bisectorRad = math.acos((bm**2 + bc**2 - hypMid**2)/(2*bm*bc))
print(bisectorRad)
print(f'{math.degrees(bisectorRad)}°')


# screw all that noise^  
# The following solution is way more straightforward.
hyp = math.hypot(ab, bc)
answer = round(math.degrees(math.acos(bc/hyp)))
print(f'{answer}°')

