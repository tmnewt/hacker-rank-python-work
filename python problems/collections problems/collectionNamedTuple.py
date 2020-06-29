# https://www.hackerrank.com/challenges/py-collections-namedtuple/problem?h_r=next-challenge&h_v=zen

from collections import namedtuple

# actual solution 
n = int(input())
Student = namedtuple('Student', input())
total = 0
for _ in range(n):
    pupil = Student(*input().split())
    total += int(pupil.MARKS)
    
print(total/n)








# some examples of usage:
# a very fun usage
Point = namedtuple('Point', 'x,y')
pt1 = Point(1,2)
pt2 = Point(3,4)
# mock dot product
dot_product = pt1.x * pt2.x  + pt1.y *pt2.y
print(dot_product)

# another interesting usage.
Car = namedtuple('Car', 'PRICE Mileage Color Make')
myCar = Car(30000, Mileage = 35, Color = 'Silver', Make = 2020)
print(myCar)
# wtf! wow, that's so nice.
print(myCar.Color)
# damn! this is so convenient
newCar = Car(*[24000, 21, 'Black', 2013])
print(newCar)