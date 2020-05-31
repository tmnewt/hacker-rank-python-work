# calculate fines (if any) according to the follwing fee structure.

# if before due date, no fine.
# if after due date but within the same calendar month and year
#       of the required date, then fine = 15 * days late
# if after the calendar month but within the same year,
#       then fine = 500 * number of months late
# if after the calendar year, fine = 10000.
#
# USE THE LEAST PRECISE MEASURE OF LATENESS. Whether it was due 
# January 1, 2017 or December 31, 2017, a book returned on January
# 1st, 2018 is considered a year late!
# #

# d1, m1, y1: refers to the return date (dd/mm/yyyy)
# d2, m2, y2: refers to the due date (dd/mm/yyyy)

# constraints:
#   1 <= d1, d2 <= 31
#   1 <= m1, m2 <= 12
#   1 <= y1, y2 <= 3000
# guarantee that all dates will be valid Gregorian calendar dates.

def libraryFine(d1, m1, y1, d2, m2, y2):
    if y1 > y2:
        return 10000
    elif (m1 > m2) and (y1 == y2):
        return (m1-m2)*500
    elif (d1 > d2) and (m1 == m2) and  (y1 == y2):
        return (d1-d2)*15
    else:
        return 0

print(libraryFine(9, 6, 2015, 6, 6, 2015)) # fine 45
print(libraryFine(9, 4, 2014, 7, 7, 2014)) # no fine
print(libraryFine(9, 7, 2014, 9, 6, 2014)) # fine 500
print(libraryFine(9, 12, 2014, 9, 1, 2014)) # fine 5500
print(libraryFine(9, 7, 2015, 9, 6, 2014)) # fine 10000
print(libraryFine(10, 7, 2014, 9, 6, 2015)) # no fine
print(libraryFine(15, 7, 2014, 1, 7, 2015))