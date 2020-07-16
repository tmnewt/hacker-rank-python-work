# https://www.hackerrank.com/challenges/decorators-2-name-directory/problem

import operator


def person_lister(f):
    def inner(people: list):
        for p in people: p[2] = int(p[2])
        return map(f, sorted(people, key= operator.itemgetter(2))) 
    return inner


# required code
@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    people = [input().split() for i in range(int(input()))]
    print(*name_format(people), sep='\n')