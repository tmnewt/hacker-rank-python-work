# given a string;

import timeit


# within string:
# '<' represents hitting the home button
# '>' represents hitting the end key
# '*' represents hitting the backspace
# '#' represents hitting the NumLock key

def receivedTextOld(s: str):
    result = []
    digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    numlock = True
    home = False  # true if the home button has been hit. stays true until end is hit
    appendix = 0
    for i in s:
        if i == '#': numlock = not numlock
            # print(f'numlock is now {numlock}')

        elif i == '<':
            # print('move to front')
            home = True
            appendix = 0
            
        elif i == '>': home = False
            # print('move to back')
            
        elif i == '*':
            try:
                if home:
                    if appendix != 0:
                        result.pop(appendix-1)
                        appendix -= 1
                else: result.pop()
                    # print('deleting from end')
            except: pass

        elif (numlock == True) and (i in digits):
            if home:
                # print(f'appending digit to {appendix}')
                result.insert(appendix, i)
                appendix += 1
            else:             
                # print(f'appending digit to end')
                result.append(i)

        elif i not in digits:
            if home:
                result.insert(appendix, i)
                appendix += 1
            else:
                result.append(i)

        #print(''.join(result))
    
    return ''.join(result)
            


def receivedTextPrint(s):
    result = ''
    digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    numlock = True
    home = False  # true if the home button has been hit. stays true until end is hit
    appendix = 0
    for i in s:
        print(f'string: {result}')
        if i == '#': 
            numlock = not numlock
            print(f'numlock is now {numlock}')

        elif i == '<':
            print('move to front')
            home = True
            appendix = 0
            
        elif i == '>': 
            home = False
            print('move to back')

        elif i == '*':
            try:
                if home:
                    if appendix != 0:
                        if appendix == 1:
                            print(f'Delete at index {appendix}')
                            print(f'Before: {result}')
                            result = result[appendix:]
                            print(f'After : {result}')
                            appendix -= 1 
                        else:
                            print(f'Delete at index {appendix}')
                            print(f'Before: {result}')
                            temp = result[:appendix]
                            print(f'temp = {temp}')
                            result = temp + result[appendix:]
                            print(f'After : {result}')
                            appendix -= 1
                                            
                else:
                    print('Delete from end')
                    print(f'Before: {result}')
                    result = result[:-1]
                    print(f'After : {result}')

            except: pass

        elif (numlock == True) and (i in digits):
            if home:
                if appendix == 0:
                    print(f'Insert {i} at front')
                    print(f'Before: {result}')
                    result = i + result
                    print(f'After : {result}')
                    appendix += 1
                else:
                    print(f'Insert {i} at {appendix}')
                    print(f'Before: {result}')
                    temp = result[:appendix] + i
                    result = temp + result[appendix:]
                    print(f'After : {result}')
                    appendix += 1
            else:             
                print(f'Insert {i} to end')
                print(f'Before: {result}')
                result = result + i
                print(f'After : {result}')

        elif i not in digits:
            if home:
                if appendix == 0:
                    print(f'Insert {i} at front')
                    print(f'Before: {result}')
                    result = i + result
                    print(f'After : {result}')
                    appendix += 1
                else:
                    print(f'Insert {i} at {appendix}')
                    print(f'Before: {result}')
                    temp = result[:appendix] + i
                    print(f'temp = {temp}')
                    result = temp + result[appendix:]
                    print(f'After : {result}')
                    appendix += 1
            else:
                print(f'Append {i} to end')
                print(f'Before: {result}')
                result = result + i
                print(f'After : {result}')


    return result
        

def receivedText(s: str):
    result = ''
    digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    numlock = True
    home = False  # true if the home button has been hit. stays true until end is hit
    appendix = 0
    for i in s:
        if i == '#': 
            numlock = not numlock

        elif i == '<':
            home = True
            appendix = 0
            
        elif i == '>': 
            home = False

        elif i == '*':
            try:
                if home:
                    if appendix != 0:
                        if appendix == 1:
                            result = result[appendix:]
                            appendix -= 1 
                        else:
                            temp = result[:appendix-1]
                            result = temp + result[appendix:]
                            appendix -= 1
                                            
                else:
                    result = result[:-1]

            except: pass

        elif (numlock == True) and (i in digits):
            if home:
                if appendix == 0:
                    result = i + result
                    appendix += 1
                else:
                    
                    result = result[:appendix] + i + result[appendix:]
                    appendix += 1
            else:             
                result = result + i

        elif i not in digits:
            if home:
                if appendix == 0:
                    result = i + result
                    appendix += 1
                else:
                    temp = result[:appendix] + i
                    result = temp + result[appendix:]
                    appendix += 1
            else:
                result = result + i
    return result

#print(receivedTextOld('He*<LL>0_>WO<*L**>D<...<#9854j*<abc<d9H#9>a'))
#print(receivedText('He*<LL>0_>WO<*L**>D<...<#9854j*<abc<d9H#9>a'))
#print(receivedTextPrint('He*<LL>0_>WO<*L**>D<...<#9854j*<abc<d9H#9>a'))




#print(timeit.timeit('''
#
#def receivedTextOld(s: str):
#    result = []
#    digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#    numlock = True
#    home = False  # true if the home button has been hit. stays true until end is hit
#    appendix = 0
#    for i in s:
#        if i == '#': numlock = not numlock
#            # print(f'numlock is now {numlock}')
#
#        elif i == '<':
#            # print('move to front')
#            home = True
#            appendix = 0
#            
#        elif i == '>': home = False
#            # print('move to back')
#            
#        elif i == '*':
#            try:
#                if home:
#                    if appendix != 0:
#                        result.pop(appendix-1)
#                        appendix -= 1
#                else: result.pop()
#                    # print('deleting from end')
#            except: pass
#
#        elif (numlock == True) and (i in digits):
#            if home:
#                # print(f'appending digit to {appendix}')
#                result.insert(appendix, i)
#                appendix += 1
#            else:             
#                # print(f'appending digit to end')
#                result.append(i)
#
#        elif i not in digits:
#            if home:
#                result.insert(appendix, i)
#                appendix += 1
#            else:
#                result.append(i)
#
#        #print(''.join(result))
#    
#    return ''.join(result)
#
#green = 'He*<LL>0_>WO<*L**>D<...<#9854j*<a'
#eggs = '<a>a'*200000
#spam = green + eggs + 'bc<d9H#9>a'
#
#b = receivedTextOld(spam)
#
#''', number= 1))
#

eggs = 'start<a<#9bZa*>>>>7737<<<2749###<######205xxw***<***j3gj2'
a = receivedTextOld(eggs)
b = receivedText(eggs)

print(a == b)
print(a)
print(b)


#print(timeit.timeit('''
#
#def receivedText(s: str):
#    result = ''
#    digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
#    numlock = True
#    home = False  # true if the home button has been hit. stays true until end is hit
#    appendix = 0
#    for i in s:
#        if i == '#': 
#            numlock = not numlock
#
#        elif i == '<':
#            home = True
#            appendix = 0
#            
#        elif i == '>': 
#            home = False
#
#        elif i == '*':
#            try:
#                if home:
#                    if appendix != 0:
#                        if appendix == 1:
#                            result = result[appendix:]
#                            appendix -= 1 
#                        else:
#                            temp = result[:appendix-1]
#                            result = temp + result[appendix:]
#                            appendix -= 1
#                                            
#                else:
#                    result = result[:-1]
#
#            except: pass
#
#        elif (numlock == True) and (i in digits):
#            if home:
#                if appendix == 0:
#                    result = i + result
#                    appendix += 1
#                else:
#                    temp = result[:appendix] + i
#                    result = temp + result[appendix:]
#                    appendix += 1
#            else:             
#                result = result + i
#
#        elif i not in digits:
#            if home:
#                if appendix == 0:
#                    result = i + result
#                    appendix += 1
#                else:
#                    temp = result[:appendix] + i
#                    result = temp + result[appendix:]
#                    appendix += 1
#            else:
#                result = result + i
#    return result
#
#ham = 'start<a>#9bZa*>>>>7737<<<2749###<######205xxw***<***j3gj2'*20000
#
#b = receivedText(ham)
#
#''',number=1))

#
#
#ham = 'start<a>#9bZa*>>>>7737<<<2749###<######205xxw***<***j3gj2'*j
##spam = green + ham + 'bc<d9H#9>a'
#
#c = receivedTextOld(ham)
#d = receivedText(ham)
#print(c == d)
#print(c)
#print(d)
#
#print(len(ham))

def receivedTextNew(s: str):
    stacks = []
    stack = ''
    last = ''
    digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    numlock = True
    home = False
    for i in s:
        if i == '#':
            numlock = not numlock

        elif i == '<':
            stacks.append(stack)
            home = True
            stack = ''

        elif i == '>':
            stacks.append(stack)
            home = False
            stack = ''

        elif i == '*':
            if home:
                if stack == '':
                    pass
                else:
                    stack = stack[:-1]
            else:
                if last == '':
                    pass
                else:
                    last = last[:-1]

        elif numlock and (i in digits):
            if home:
                stack = stack + i
            else:
                last = last + i

        elif i not in digits:
            if home:
                stack = stack + i
            else:
                last = last + i

    stacks.append(stack)
    result = ''
    for _ in range(len(stacks)):
        result = result + stacks.pop()

    return result + last


print(receivedTextNew(eggs))




print(timeit.timeit('''
def receivedTextNew(s: str):
    stacks = []
    stack = ''
    last = ''
    digits = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    numlock = True
    home = False
    for i in s:
        if i == '#':
            numlock = not numlock

        elif i == '<':
            stacks.append(stack)
            home = True
            stack = ''

        elif i == '>':
            stacks.append(stack)
            home = False
            stack = ''

        elif i == '*':
            if home:
                if stack == '':
                    pass
                else:
                    stack = stack[:-1]
            else:
                if last == '':
                    pass
                else:
                    last = last[:-1]

        elif numlock and (i in digits):
            if home:
                stack = stack + i
            else:
                last = last + i

        elif i not in digits:
            if home:
                stack = stack + i
            else:
                last = last + i

    stacks.append(stack)
    result = ''
    for _ in range(len(stacks)):
        result = result + stacks.pop()

    return result + last


ham = 'start<a>#9bZa*>>>>7737<<<2749###<######205xxw***<***j3gj2'*20000

b = receivedTextNew(ham)

''', number= 1))