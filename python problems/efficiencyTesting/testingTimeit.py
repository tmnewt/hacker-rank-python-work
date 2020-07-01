# yes this file is literally for testing related to preparing and running snipits of code in Timeit

from timeit import timeit

# which is faster? defining a function with the statement or within the setup?

# first with the function defined in statement
print(timeit('''
def dumbFunction(arr: list):
    newList = [x+1 for x in arr]

dum = dumbFunction(myArr)
''', setup= 'myArr = [1,2,3,4,5]'))

# now with the function defined in the setup
toSetup = '''
myArr = [1,2,3,4,5]
def dumbFunction(arr: list):
    newList = [x+1 for x in arr]'''
print(timeit('dum = dumbFunction(myArr)', setup= toSetup))

# The evidence is clear. It is obvious that defining objects at setup cuts down on BS processing time.