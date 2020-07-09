# https://www.hackerrank.com/challenges/python-quest-1/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

# just add repunits

for i in range(1,int(input())): #More than 2 lines will result in 0 score. Do not leave a blank line also
    print(i*((10**i-1)//9))