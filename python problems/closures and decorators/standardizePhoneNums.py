# https://www.hackerrank.com/challenges/standardize-mobile-number-using-decorators/problem

def wrapper(func):
    def mobileNumFormater(l):
        mobileNumbers = []
        for line in l:
            first5 = line[-10:][:5]
            last5 = line[-5:]
            mobileNumbers.append(f'+91 {first5} {last5}')
        return func(mobileNumbers)
        
    return mobileNumFormater


# Top upvoted wrapper designed by someone in the solution comments
def betterWrapper(f):
    def phonenum(lines):
            f([f'+91 {line[-10:-5]} {line[-5:]}' for line in lines])
    return phonenum

@betterWrapper
def sort_phone_nums(l: list):
    print(*sorted(l), sep= '\n')


# Code given
@wrapper
def sort_phone(l):
    print(*sorted(l), sep='\n')
if __name__ == '__main__':
    l = [input() for _ in range(int(input()))]
    sort_phone(l)
    sort_phone_nums(l)
