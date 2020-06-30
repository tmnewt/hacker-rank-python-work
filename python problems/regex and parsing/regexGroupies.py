# https://www.hackerrank.com/challenges/re-group-groups/problem


import re

# The problem's solution.

mat = re.match(r'.*?([a-zA-Z0-9])\1.+', input())
try: print(mat.group(1))
except: print('-1')

# the above can be replicated with
mat = re.search(r'([a-zA-Z0-9])\1', input())
try: print(mat.group(1))
except: print('-1')

#notice the difference between search and match.



# some other useful things:

m = re.match(r'(\w+)@(\w+)\.(\w+)','username@gmail.com')
print(m)
print(type(m))
for i in range(4):
    print(m.group(i))
print(m.group(0,1,2,3))

try:
    print(m.group(5))
except IndexError:
    print('IndexError: no such group exists')

# groups() returns only subgroups of the match
print(m.groups())

# groupdict() does exactly what you think except it won't work if 
# the dictionary keys weren't defined in the regular expression
print(m.groupdict())

a = re.match(r'(?P<user>\w+)@(?P<website>\w+)\.(?P<extension>\w+)','myname@hackerrank.com')
print(a.groupdict())



