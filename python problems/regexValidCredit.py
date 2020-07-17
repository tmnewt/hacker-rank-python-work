# https://www.hackerrank.com/challenges/validating-credit-card-number/problem?h_r=next-challenge&h_v=zen

# I love this problem because I leanred so much from it!

# Side note, I have yet to figure out if it is possible to create a single expression
# which doesn't make use of ad hoc string formating or python conditional statements
# It's honestly not worth the time to craft a precise and eloquent expression when
# chaining multiple expressions is more developer friendly and has insignificant
# tradeoffs.


import re

structureExpr = r'^[456]([\d]{15}|[\d]{3}(-[\d]{4}){3})$'
consecutiveRepeatExpr = r'^((\d)-?(?!(-?\2){3})){16}$'

for _ in range(int(input())):
    s = input()
    if (re.match(structureExpr, s) != None) and (re.match(consecutiveRepeatExpr, s) != None):
        print('Valid')
    else:
        print('Invalid')


# NOTES ON COMBINING EXPRESSION PATTERNS
#
# =============================================
# structureExpr = r'^[456]([\d]{15}|[\d]{3}(-[\d]{4}){3})$'
#
# ^ means string must be start of line
#   [456] first char must be 4 5 or 6
#       ([\d]{15}|[\d]{3}(-[\d]{4}){3}) 
#           next 15 char must be digits
#            OR
#           \d\d\d then followed by -\d\d\d\d   3 times  
# Lastly $ means the pattern must end
# 
#   All this guarantees the string is 16 digits  OR  is the form 4digits-4digits-4digits-4digits   
#
# ============================================
# 
# ConsecutiveRepeatExpr = r'^((\d)-?(?!(-?\2){3})){16}$'
# Yes, I am aware this expression seems counter intuitive to what we are solving for.
# I am aware that a string such as '2-2-5-3-62-5-8-79-6-1-5786' would match the consecutive repeating expression
# On it's own this expression would not work as the solution. But combine it with the StructureExpr in the form of
# simultaneous conditional statements and it suddenly becomes useful.
# 
# ^ start anchor (technically not needed because of structure Expr)
#   ((\d)-?(?!(-?\2){3})){16}  the first capture group and the requirement of 16 DIGITS. 
#       (\d) second capture group a.k.a the important part
#           -?  optional hypthen. Necessary to cover both pure 16 digit format and the hypthen format.
#              (?!(-?\2){3}) negative look ahead. If there are 4 consecutive digits, even if seperated by a hypthen,
#                               then the string is discarded. 
# 
# #
