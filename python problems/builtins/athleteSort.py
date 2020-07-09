# https://www.hackerrank.com/challenges/python-sort-sort/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

#table = [
#    [10,2,5],
#    [7,1,0],
#    [9,9,8],
#    [1,23,12],
#    [6,5,9]]
#k = 1


n, m = list(map(int, input().split()))
table = [list(map(int, input().split())) for _ in range(n)]
k = int(input())
newTable = sorted(table, key=lambda athletes: athletes[k])
#print(newTable)
for i in newTable:
    print(' '.join(list(map(str,i))))
