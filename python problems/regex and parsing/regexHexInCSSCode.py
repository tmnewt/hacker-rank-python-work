

import re

expr = re.compile(r'.(#[A-Fa-f\d]{3}[A-Fa-f\d]?[A-Fa-f\d]?[A-Fa-f\d]?)\b')
# other expression: r'.(#[a-fA-F\d]{6}|#[a-fA-F\d]{3})\b'
n = int(input())
res = []
for _ in range(n):
    res += re.findall(expr, input())

for each in res:
    print(each)




#
#a = []
#test = 'color: #FfFdF8; background-color:#aef;'
#b = re.findall(expr, test)
#a += b
#print(a)
#
#test = '#BED'
#s = re.findall(expr, test)
#print(s)
#a += s
#print(a)