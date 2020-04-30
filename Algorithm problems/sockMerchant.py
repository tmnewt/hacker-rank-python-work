#matching and removing
#[1, 1, 2, 1, 2, 1, 1, 4, 4]
# i = 0   j = 1  
# [2, 1, 2, ]
# 
# 
# 
# 
# 
#def sockMerchant(n, ar):
#    pair = 0
#    outer_trigger = False
#    for i in range(n):
#        try:
#            inner_trigger = False
#            for j in range(n):
#                try:
#                    if (ar[i] == ar[j]) and (i!=j):
#                        if i<j:
#                            ar.pop(j)
#                            ar.pop(i)
#                        else:
#                            ar.pop(i)
#                            ar.pop(j)
#                        pair += 1
#                except IndexError:
#                    inner_trigger = True
#                if inner_trigger == True:
#                    break
#        except IndexError:
#            outer_trigger = True
#        if outer_trigger == True:
#            break
#    for i in range(len(ar)):
#        if ar[i] == ar[-1]:
#            ar.pop()
#            pair += 1
#            break
#    return pair
#
arr = [10, 20, 20, 10 ,10, 30, 50, 10, 20]
arr_test2 = [20, 20, 10, 10, 10, 4, 3, 10, 3, 4, 1, 2, 6, 12, 12]
arr_load3 = '6 5 2 3 5 2 2 1 1 5 1 3 3 3 5'
arr_test3 = list(map(int, arr_load3.rstrip().split()))

#def junk_function(ar):  # function that does nothing interesting
#    trigger = False
#    for i in range(20):
#        try:
#            print(ar[i])
#        except IndexError:
#            trigger = True
#        if trigger == True:
#            print('time to stop')
#            break
            
#junkfunc(arr)

#print(sockMerchant(len(arr_test3), arr_test3))
#
#def sockMerchantlog(ar):
#    n = len(ar)
#    log = ''
#    pair = 0
#    outer_trigger = False
#    for i in range(n):
#        try:
#            log += f'current list is: {ar}\n'
#            log += f'testing value: {ar[i]} at index : {i}\n'
#            inner_trigger = False
#            for j in range(n):
#                try:
#                    if (ar[i] == ar[j]) and (i!=j):
#                        if i<j:
#                            ar.pop(j)
#                            ar.pop(i)
#                        else:
#                            ar.pop(i)
#                            ar.pop(j)
#                        pair += 1
#                        log += f'found a pair! Current count is: {pair}\n'
#                        log += f'breaking out from current loop\n'
#                        break
#                except IndexError:
#                    inner_trigger = True
#                if inner_trigger == True:
#                    log += f'while looking for a pair for {ar[i]}, iteration went out side of bounds. There are logically no pairs.\n'
#                    break
#        except IndexError:
#            outer_trigger = True
#        if outer_trigger == True:
#            break
#    log += f'doing a pass on the last index.\n'
#    for i in range(len(ar)):
#        if ar[-1] == ar[i]:
#            ar.pop()
#            ar.pop(i)
#            pair += 1
#            log += f'found a pair!\n'
#            break
#    log += f'finall pair count is: {pair}'
#    return log
#
##print(sockMerchantlog(arr_test3))
#
def newsockMerchant(n, ar):
    pair = 0
    trigger = True
    while trigger:
        print(f'current array is {ar} with length of {len(ar)} and ending value of {ar[-1]}')
        for i in range(len(ar)):
            print(f'current i is: {i}')
            if i == len(ar)-1:
                ar.pop()
                break
            
            if ar[-1] == ar[i]:
                print(f'found match ')
                ar.remove(ar[i])
                ar.pop()
                pair += 1
                break
            
        if (len(ar) == 1) or (len(ar) == 0):
            trigger = False
    return pair



print(newsockMerchant(15, arr_test3))

