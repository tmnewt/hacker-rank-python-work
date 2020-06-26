# given a string;

import timeit


# within string:
# '<' represents hitting the home button
# '>' represents hitting the end key
# '*' represents hitting the backspace
# '#' represents hitting the NumLock key

def receivedText(s):
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
            
print(receivedText('He*<LL>0_>WO<*L**>D<...<#9854j*<abc<d9H#9>a'))



        
