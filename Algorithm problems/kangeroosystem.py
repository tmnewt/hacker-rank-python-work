# test cases failed:

tests = []
                                    # EXPECTED Output:
tests.append('0 2 5 3')             # NO
tests.append('21 6 47 3')           # NO
tests.append('1817 9931 8417 190')  # NO
tests.append('112 9563 8625 244')   # NO
tests.append('2 3 94 2')            # YES
tests.append('23 9867 9814 5861')   # NO



start_1 = 21
vel_1 = 6
start_2 = 47
vel_2 = 3

def kangaroo(x1, v1, x2, v2):
    # find the positive value intersection of a given system
    
    # catch for parallel
    if v1 <= v2:
        return 'NO'
    # catch for same start
    if x1 == x2:
        return 'YES'
    
    # solve for x-coordinate of intersection    
    calc = (x2-x1)%(v1-v2)
    if calc == 0:
        return 'YES'
    else:
        return 'NO'
     
     

    
for test in tests:
    arguments = test.split()
    start_1 =   int(arguments[0])
    vel_1 =     int(arguments[1])
    start_2 =   int(arguments[2])
    vel_2 =     int(arguments[3])
    print(kangaroo(start_1, vel_1, start_2, vel_2))

