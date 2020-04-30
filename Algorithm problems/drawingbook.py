# n = number of pages in a book
# p = page to turn to.
# return the minimum number of turns to reach the required page given that you can start from either the front or the back of the book.

# even numbers are on the left side of the book
# odd numbers are on the right side of the book



# for example: if n = 15 and p = 7
#       the desired page would be 3 from the front and 4 pages from the back.
# another example:  n = 15, p = 8
#       then 4 pages from front and 3 from back
# another example: n  = 16, p = 7
#       then 3 pages from front and 5 from back
# another example: n = 16, p = 8 
#       then 4 pages from front and 4 from back
# another example: n = 15, p = 10
#       then 4 pages from front and 2 from back
#       shares same result as n = 14, p = 10 and n = 14, p =11, n =15, p=11
# 

def pageCount(n, p):
    if n%2 == 1: #last number is odd
        n = n-1
    if p%2 == 1: #odd page number.
        p = p-1

    return int(min(p/2,(n-p)/2))

print(pageCount(200, 101))








