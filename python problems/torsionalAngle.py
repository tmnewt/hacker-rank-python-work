# https://www.hackerrank.com/challenges/class-2-find-the-torsional-angle/problem?isFullScreen=false&h_r=next-challenge&h_v=zen

# Finish the premade Points Class so that it prints the torsion angle
# Possiblely one of the most difficult challenges because it's math!
import math

class Points(object):
    def __init__(self, x, y, z):
        self.x = x; self.y = y; self.z = z

    def __sub__(self, p): # I'm annoyed so I'm going to format things weirdly...
        return Points(
            self.x - p.x,
            self.y - p.y,
            self.z - p.z)

    def dot(self, p): 
        return (
            self.x * p.x
          + self.y * p.y
          + self.z * p.z)

    def cross(self, p):
        return Points(
            self.y * p.z - self.z * p.y,
            self.z * p.x - self.x * p.z,
            self.x * p.y - self.y * p.x)

        
    def absolute(self): 
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)

if __name__ == '__main__':
    points = list()
    for i in range(4):
        a = list(map(float, input().split()))
        points.append(a)

    a, b, c, d = Points(*points[0]), Points(*points[1]), Points(*points[2]), Points(*points[3])
    x = (b - a).cross(c - b)
    y = (c - b).cross(d - c)
    angle = math.acos(x.dot(y) / (x.absolute() * y.absolute()))

    print("%.2f" % math.degrees(angle))