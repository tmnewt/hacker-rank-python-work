test = [1,1,2,2,4,4,5,5,5]  #answer = 5
test2 = [4,6,5,3,3,1] # answer = 3
test3 = [1,2,2,3,1,2] # answer = 5

def pickingNumbers(a: list):
    maximum = 0
    completedints = []
    for i in range(len(a)):
        if a[i] not in completedints:
            #print(f'examine {a[i]}')
            examined_lowers = 1
            examined_highers = 1
            for j in range(len(a)):
                #print(f'comparing {a[j]}')
                if (i!=j):
                    if (abs(a[i]-a[j]) <= 1) and (a[i] >= a[j]):
                        #print('picked lowers!')
                        examined_lowers += 1
                    if (abs(a[i]-a[j]) <= 1) and (a[i] >= a[j]):
                        #print('picked highesr!')
                        examined_highers += 1
            examined = max(examined_lowers, examined_highers)
            completedints.append(a[i])
            if examined > maximum:
                #print(f'new max found! {examined}')
                maximum = examined
        #else:
            #print(f'skip {a[i]}')
    return maximum 


print(pickingNumbers(test))
print('\n')
print(pickingNumbers(test2))
print('\n')
print(pickingNumbers(test3))





# maximumthing = 0


# [1, 1, 2, 3, 4, 4, 6]

# look at 0 index, which is 1
# Arrays
# 2 length arrays
# [1,1]

# if len(^thatthing) is greater than the maximumthing
    # then update maximumthing = len(^thatthing)


# [1,2] = [2,1] <--- only interested in length, so pos doesn't matter
# 3 length arrays
# [1, 1, 2] 



# look at 1 index, which is 1:
# exact same thing as above:

# look at 2 index, which just so happens to be 2
# 2 length arrays
# [1, 2]
# [1, 2] <= no new info
# [2, 3]
# 3 length array
# [1,1,2]

# look at 3 index, which just so happens to be 3
# 2 length array:
# [2,3]
# [3,4]
# [3,4]
# 3 length array:
# [3, 4, 4]

# [1, 1, 2, 3, 4, 4, 6]

