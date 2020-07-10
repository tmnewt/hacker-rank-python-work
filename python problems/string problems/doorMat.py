# https://www.hackerrank.com/challenges/designer-door-mat/problem




def doorMat(h: int, l: int):
    welcome = 'WELCOME'
    pat = '.|.'
    hMid = (h+1)//2
    # top
    n = 1 
    for _ in range(1,hMid):
        padding = '-'*((l-3*n)//2)
        print(padding + pat*n + padding)
        n += 2

    # middle
    midpadding = '-'*((l-7)//2)
    print(midpadding + welcome + midpadding)
    
    #bottom
    n-=2
    for i in range(hMid-1,0,-1):
        padding = '-'*((l-3*n)//2)
        print(padding + pat*n + padding)
        n -= 2
    

doorMat(30,90)



# Notes:
#   size = h * l
#   h is always odd
#   l = 3*h
#   WELCOME takes up 7 spaces
#   .|. is the patern to use
#   it increases by 2 each step
#   until midpoint. 
# 
#  
# sample patters
#
#    Size: 7 x 21 
#    ---------.|.---------      <-- padding = (length - pat*i)/2
#    ------.|..|..|.------
#    ---.|..|..|..|..|.---
#    -------WELCOME-------      <-- h midpoint = (h+1)/2
#    ---.|..|..|..|..|.---
#    ------.|..|..|.------
#    ---------.|.---------
# 
#              ^ l midpoint = (l+1)/2
# 
# 
#
# Some more patterns  
#
#    Size: 11 x 33
#    ---------------.|.---------------
#    ------------.|..|..|.------------
#    ---------.|..|..|..|..|.---------
#    ------.|..|..|..|..|..|..|.------
#    ---.|..|..|..|..|..|..|..|..|.---
#    -------------WELCOME-------------
#    ---.|..|..|..|..|..|..|..|..|.---
#    ------.|..|..|..|..|..|..|.------
#    ---------.|..|..|..|..|.---------
#    ------------.|..|..|.------------
#    ---------------.|.---------------
#
# 
#
#    Size: 9 x 27
#    ------------.|.------------
#    ---------.|..|..|.---------
#    ------.|..|..|..|..|.------
#    ---.|..|..|..|..|..|..|.---
#    ----------WELCOME----------
#    ---.|..|..|..|..|..|..|.---
#    ------.|..|..|..|..|.------
#    ---------.|..|..|.---------
#    ------------.|.------------
#