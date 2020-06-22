# https://www.hackerrank.com/challenges/string-validators/problem?h_r=internal-search

def stringValidator(s: str):
    s = list(s)
    # has
    alphaNum = False; alphabetical = False; digits = False
    lowercase = False; uppercase = False
    for i in s:
        if (alphaNum == True) and (alphabetical == True) and (
            digits == True) and (lowercase == True) and (
            uppercase == True):
            break
        if i.isalnum():
            alphaNum = True
        if i.isalpha():
            alphabetical = True
        if i.isdigit():
            digits = True
        if i.islower():
            lowercase = True
        if i.isupper():
            uppercase = True
        
    print(alphaNum)
    print(alphabetical)
    print(digits)
    print(lowercase)
    print(uppercase)

test = 'qA2'
stringValidator(test)
    


