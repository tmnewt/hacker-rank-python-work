# https://www.hackerrank.com/challenges/day-of-the-programmer/problem?h_r=internal-search

def dayOfProgrammer(year):
    base = 215 # 31 (Jan) + 31 (March) +30 (April) +31 (May) +30 (June) +31 (July) +31 (August)
    if year >= 1919:
        if (year%4 ==0) and (year%100 != 0):
            return f'{256 - (base+29)}.09.{year}'

        elif year%400 == 0:
            return f'{256 - (base+29)}.09.{year}'

        else:
            return f'{256 - (base+28)}.09.{year}'

    if year == 1918:
        return f'{256-(base+15)}.09.{year}'
        
    if year < 1918:
        if year%4 == 0:
            return f'{256 - (base+29)}.09.{year}'
        else:
            return f'{256 - (base+28)}.09.{year}'


print(dayOfProgrammer(1900))