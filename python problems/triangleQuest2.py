# https://www.hackerrank.com/challenges/triangle-quest-2/problem

# can't use more than 2 lines. Must use the following for loop
# can't use strings. Everything must be pure maths

'''Notice that each line is 1(repeat i times)^2

1^2 = 1
11^2 = 121
111^2 = 12321
1111^2 = 1234321
etc...

Too bad we can't use strings generate repeating 1's!

fortunately we can use the following to generate an i length of 1's:
    (10^i-1)/9  which will give 1, 11, 111, 1111 etc.
    be careful that the above will return a float so use // 
'''


for i in range(1, int(input())+1):
    repeating1 = (10**i-1)//9
    print(repeating1**2)


