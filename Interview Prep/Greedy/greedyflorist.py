# https://www.hackerrank.com/challenges/greedy-florist/problem
#
# An insane florist wants to drive away all of his customers by jacking up
#   the price of his flowers. His strategy is to charge each individual 
#   customer (n + 1) * starting flower price, where n is the number of
#   flowers the customer previously purchased today. Each purchase is 
#   itemized, meaning each flower is rung up as an individual purchase.
#   So, if a new customer purchases 4 flowers where the original price is $5,
#   then the math works out as follows
#     ---------------------------------- 
#     |1st flower| (0 + 1) * 5 = |   5  |
#     |2nd flower| (1 + 1) * 5 = |  10  |
#     |3rd flower| (2 + 1) * 5 = |  15  |
#     |4th flower| (3 + 1) * 5 = |  20  |
#     |Total cost|             = | $50  |
#
# Despite his strategy, the florist ends up as the only florist in town...
# 
# But his customers have gotten smart. Now customers buy flowers as a 
#   group, thereby allowing them to purchase more flowers as a group,
#   than if they had ordered by themselves. This also helps them 
#   minimize the total cost. For instance if a group of 3 customers
#   purchases the same 4 flowers like in the earlier example then they
#   are only charged $5 for the first 3 flowers (because each member of
#   the group purchased a single flower) and the 4th flower costs $10,
#   (because 1 of the members had to go up again). So in total they paid,
#   only $25. 
# 
# Anyway, the given a set of flowers with there original prices, and a 
#   group of K members, calculate the minimum cost to purchase the set. 
#
# 
# Constraints
# 1 <= The set size of flowers and number of members of a group <= 100
# 1 <= the original price of each flower <= 10^6
# the answer is < 2^31
# 
# This is extremely easy. 
# take the given flower cost list "c" and sort it. 
# Now create a members list of length K and set each value in the list to 1 (saves from doing n + 1) 
#   set an index variable m that will be used to access the members list.
#   
# Iterate over the costs list using a while loop that continues until the
#   costs list is empty. 
#   pop the costs list. This will be largest cost. Go to the members list and
#   pick the first sucker. multiply their member value by the cost and add the
#   product to the total cost. Then increment the member's value by 1, to reflect
#   that it will cost them more on the next purchase.
#   If the members list raises an index error when given index variable "m" it 
#   means we've reached the end of the member list and it's time to cycle back around,
#   
#   return the total value at the end...
# 
# #


def getMinimumCost(k, c):
    total = 0
    c = sorted(c)
    mems = [1]*k
    m = 0
    while len(c) != 0:
        cost = c.pop()
        try:
            total += mems[m]*cost
        except IndexError:
            m = 0
            total += mems[m]*cost
        mems[m] += 1
        m += 1
    return total

costs = [9,3,1,5,7]
print(getMinimumCost(3,costs))