import math

# find number of squares inclusive in range.
# for example, how many perfect squares are there in the range a to b
#

# don't do precomputation attack...

#test = 9
#sroot = test**(1/2)
#if sroot == int(sroot):
#    print(int(sroot))


# 1 to 12
# [1, 2.... 12]

# is 1 a square root yes  1^2
# is 2 a squ no
# 3 no
# 4 yes 2^2
# 5 no
# 6 no, 7 no, 8 no,
# 9 yes 3^2
# 10 no
# 11 no
# 12 no

# 3000 to 5000
# 60 , 70 
# a^(1/2) = 54.7, 
# b^(1/2) = 70.7
# [55.... 70]

def squares(a, b):
    low = math.ceil(a**(1/2))
    print(low)
    upp = math.floor(b**(1/2))
    print(upp)
    return (upp-low)+1

print(squares(3000, 5000), '\n')

print(squares(3,9), '\n')
print(squares(17,24))
