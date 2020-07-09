
'''Some eval() stuff'''
# https://www.hackerrank.com/challenges/python-eval/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

var = input()
eval(var)


# https://www.hackerrank.com/challenges/input/problem?h_r=next-challenge&h_v=zen

# this problem isn't exclusive to python 2...

x, k = list(map(int, input().split()))
if eval(input()) == k: print('True')
else: print('False')