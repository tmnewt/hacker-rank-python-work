# https://www.hackerrank.com/challenges/any-or-all/problem

# check if any integer is a palindromic integer


n = int(input()); pints = input().split()
print(all([True if int(i)>0 else False for i in pints]) and any([i == i[::-1] for i in pints]))

