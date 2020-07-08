# https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem

# kill me

# set.remove() will raise a key error 
# set.discard() will NOT raise a key error
# set.pop() removes and return arbitrary element. if no elements raises key error

n = int(input())
s = set(map(int, input().split()))
n = int(input())
for _ in range(n):
    line = input()
    if line == 'pop':
        try:
            s.pop()
        except KeyError:
            break
    else:
        op, elm = line.split()
        elm = int(elm)
        if op == 'remove':
            try:
                s.remove(elm)
            except KeyError:
                continue
        if op == 'discard':
            s.discard(elm)    
print(sum(s))