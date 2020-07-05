# https://www.hackerrank.com/challenges/re-start-re-end/problem


import re 

def startandend(s, sub):
    if re.search(fr'({sub})', s) != None:
        matches = re.finditer(fr'(?=({sub}))', s)
        for match in matches:
            print(f'({int(match.start())}, {int(match.end())+len(sub)-1})')
    else:
        print('(-1, -1)')

line1 = input()
line2 = input()
startandend(line1, line2)


#matches= re.finditer(fr'(?=({pat}))', s)
#hell = re.search(fr'({pat})', s)
#if hell != None:
#    print('can compare')
#print(matches)
#print(type(matches))
#print(matches)
#for match in matches:
#    print(int(match.start()), int(match.end())+len(pat)-1)
    