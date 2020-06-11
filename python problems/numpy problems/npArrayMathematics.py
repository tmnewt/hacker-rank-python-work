import numpy as np

# perform and print the following operations given 2 arrays of shape N x M
# 1. Addition
# 2. Subtraction 
# 3. Multiplication
# 4. Integer Division
# 5. Mod 
# 6. Power 

n, m = map(int, input().split())
a = np.array([input().split() for _ in range(n)], int)
b = np.array([input().split() for _ in range(n)], int)

print(a+b)
print(a-b)
print(a*b)
print(a//b)
print(a%b)
print(a**b)

