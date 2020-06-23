# https://www.hackerrank.com/challenges/alphabet-rangoli/problem

# I hate this problem simply because I over thought it... 

def print_rangoli(size: int):
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
               'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
               'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    L = []
    for i in range(size):
        s = "-".join(letters[i:size])
        #print(s)
        #print(s[::-1])
        #print(s[1:])
        L.append((s[::-1]+s[1:]).center(4*size-3, "-"))
        #print(L)

    print('\n'.join(L[:0:-1]+L))

print_rangoli(26)








# Below are some patterns for reference.
# size 1

#         a

# size 2:

#       c-b-c
#       b-a-b
#       c-b-c

# size 3

#     ----c----
#     --c-b-c--
#     c-b-a-b-c
#     --c-b-c--
#     ----c----

#size 5

#     --------e--------
#     ------e-d-e------
#     ----e-d-c-d-e----
#     --e-d-c-b-c-d-e--
#     e-d-c-b-a-b-c-d-e
#     --e-d-c-b-c-d-e--
#     ----e-d-c-d-e----
#     ------e-d-e------
#     --------e--------

#size 10

#     ------------------j------------------
#     ----------------j-i-j----------------
#     --------------j-i-h-i-j--------------
#     ------------j-i-h-g-h-i-j------------
#     ----------j-i-h-g-f-g-h-i-j----------
#     --------j-i-h-g-f-e-f-g-h-i-j--------
#     ------j-i-h-g-f-e-d-e-f-g-h-i-j------
#     ----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
#     --j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
#     j-i-h-g-f-e-d-c-b-a-b-c-d-e-f-g-h-i-j
#     --j-i-h-g-f-e-d-c-b-c-d-e-f-g-h-i-j--
#     ----j-i-h-g-f-e-d-c-d-e-f-g-h-i-j----
#     ------j-i-h-g-f-e-d-e-f-g-h-i-j------
#     --------j-i-h-g-f-e-f-g-h-i-j--------
#     ----------j-i-h-g-f-g-h-i-j----------
#     ------------j-i-h-g-h-i-j------------
#     --------------j-i-h-i-j--------------
#     ----------------j-i-j----------------
#     ------------------j------------------



