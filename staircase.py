   #
  ##
 ###
####

# notice that it has spaces leading before the 'step'

n = 5


# build staircase
for i in range(n+1):
    if i != 0:    
        # describe 'air' using spaces
        step = ' '*(n-i)
        step += '#'*i
        print(step)



