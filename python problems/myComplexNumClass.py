# https://www.hackerrank.com/challenges/class-1-dealing-with-complex-numbers/problem

# Hackerrank provides most of the class code. 
# Challenge involves overriding the inbuilt operations


import math

class Complex(object):
    def __init__(self, real: float, imaginary: float):
        self.real = real
        self.imaginary = imaginary
        
    def __add__(self, cn):
        r2 = cn.real; i2 = cn.imaginary
        newR = self.real + r2
        newI = self.imaginary + i2
        return Complex(newR, newI)
        
    def __sub__(self, cn):
        r2 = cn.real; i2 = cn.imaginary
        newR = self.real - r2
        newI = self.imaginary - i2
        return Complex(newR, newI)
        
    def __mul__(self, cn):
        r2 = cn.real; i2 = cn.imaginary
        newR = self.real * r2 - self.imaginary * i2
        newI = self.real * i2 + r2 * self.imaginary
        return Complex(newR, newI)

    def __truediv__(self, cn):
        r2 = cn.real; i2 = cn.imaginary
        z = r2**2 + i2**2
        newR = (self.real * r2 + self.imaginary * i2)/z
        newI = (self.real * -i2 + r2 * self.imaginary)/z
        return Complex(newR, newI)

    def modulus(self):
        newR = math.sqrt(self.real**2 + self.imaginary**2)
        return Complex(newR, 0)

    def __str__(self):
        #ew, you can tell when this was written.
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result


# heres how it will run:
if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.modulus(), y.modulus()]), sep='\n')