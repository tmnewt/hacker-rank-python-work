# https://www.hackerrank.com/challenges/py-set-mutations/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

n =  int(input())
a = set(map(int, input().split()))
instructions = int(input())
for _ in range(instructions):
    op, junk = input().split()
    up = set(map(int, input().split()))
    eval(f'a.{op}({up})')

print(sum(a))