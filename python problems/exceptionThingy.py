# https://www.hackerrank.com/challenges/exceptions/problem

# task: handle encountering differnt errors and returning
#       correct error codes.

n = int(input())

for _ in range(n):
    try: 
        a, b = list(map(int, input().split()))
        print(a//b)
    except ValueError as valE:
        print('Error Code:', valE)
    except ZeroDivisionError as zdE:
        print('Error Code:', zdE)