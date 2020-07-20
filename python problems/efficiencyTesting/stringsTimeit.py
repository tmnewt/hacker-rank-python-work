# file for seeing how what is most efficient when it comes to strings
import timeit

# adding strings testing
appStringSetup = """ 
sArr = 'a b c d e f g h i j k l'.split()
"""


# naive concatenation using += within a for loop
print(timeit.timeit('''
spam = ''
for i in sArr:
    spam += i
''', setup= appStringSetup), ' Using the naive for loop approach:')


# join list testing
print(timeit.timeit('spam = "".join(sArr)', appStringSetup), 'Using the str.join method')

