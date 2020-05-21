# given a range of numbered days, [i...j] and a number k, determine 
# the number of days in the range that are beautiful. 
# Beautiful numbers are defined as nums where |i - reverse(i)| is evenly divisible by k
# If a day's value is a beautiful num, it is a beautiful day. 
# Print the num of beautiful days in the range.
#
# The reverse of a number is the number written backwards. For instance, the reverse of 
# 12 is 21. The reverse of 90 is 09 (or just 9). The reverse of 100 is 1. But the reverse 
# of 1 is NOT 100
# #


def beautifulDays(i, j, k):
    count = 0
    for day in range(i, j+1):
        if (abs(day - reverseint(day))%k == 0):
            count += 1 
    return count

def reverseint(num: int):
    reverse = 0
    while num>0:
        d = num % 10
        reverse = (reverse*10) + d
        num = int(num/10)
    return reverse

spam = 9083      # reverse is 3809
small_spam = 21         # reverse is 12
spam_with_zeros = 200   # reverse is 002 (simply 2)
huge_spam = 120324      # reverse is 423021
best_spam = 343000      # reverse is 000343 (simply 343)


print(beautifulDays(2003, 343000, 6))



#print(reverseint(spam))
#print(reverseint(small_spam))
#print(reverseint(best_spam))

# code talkthrough to 'reverse' a number
# on small integers this could easily be achieved with str manipulation.
# however, as the size of the integer increases the number of operations
# increases linearly. str manipultation is not the best choice

# instead, a mathematical approach might be best.
# We can grab the last digit via performing a modulo of 10 on the number.
# for instance if the number is 9083 then 9083 % 10 is 3.
# that 3 goes to the front (call this the workingdigit) 

#working_digit = spam % 10 

# we could append it as str, but a better approach would be with math.
# lets define the reverse first as a 0 

#reverse = 0

# 'appending' the working digit can be done mathematically with the following:

#reverse = (reverse * 10) + working_digit

# why do this? well, this will come important for later.
# now let's get rid of the working digit on the original number.

#spam = int(spam/10)

# now the 9083 has become 908. 
# we now repeat the process until our original number has been reversed.

