# https://www.hackerrank.com/challenges/the-birthday-bar/problem?h_r=internal-search

s = [1, 2, 1, 3, 2, 1, 2, 4, 2, 1] 
d = 3
m = 2
# given this result should be 2

count = 0
#for i in range(len(s)):
#    if i != len(s)-m+1:
#        print(sum(s[i:i+m]))
#        if sum(s[i:i+m-1]) == d:
#            count += 1
#            print('found a combination')
#    else:
#        print('stop')

for i in range(len(s)):
    if i < len(s)-m+1:
        print(f'index is {i}')
        print(f'window is {s[i:i+m]} with sum of {sum(s[i:i+m])}')
        if sum(s[i:i+m]) == d:
            count += 1

print(count)

count = 0    
# other solution?
for i in range(len(s)-m+1):
    print(f'index is {i}')
    print(f'window is {s[i:i+m]} with sum of {sum(s[i:i+m])}')
    if sum(s[i:i+m]) == d:
        count += 1   

print(count)