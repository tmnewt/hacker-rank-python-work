# given 2 players (p1 and p2)
# given p1 moves first 
# given a int n between 1 and 100 (inclusive) (game of stones)
# given each player may subtract either 2, 3, or 5 from n (remove exact amount of stones)
# if a player makes a move that causes n to go below 0 they lose.
#               This is akin to not being able to make a legal move, thus losing.
#               Conversely, winning can occur by removing the last stones.
# 
# 
# I think this can be described as a nim type game... which if it is would save me time.
# Here's what I'm thinking...
# The piles are in sizes of 5 (because 5 is largest action in this game). 
# for instance, a pile of 9 can be described as a pile of 5 and 4
#               a pile of 8 can be described as a pile of 5 and 3
#               a pile of 7 can be described as a pile of 5 and 2  
#               a pile of 6 can be described as a pile of 5 and 1
#
#   this logic describes the minimal piles that can occur for all values above 7
#
#   but there are other combinations.
#   for instance, consisder 9 stones.
#       it can be thought of as 3 piles of 3. or
#       it can be thought of as 3 piles of 2 and 1 pile of 3, or 
#       it can be thought of as 4 piles of 2 and 1 extra stone.
# 
#  #


def gameOfStones(stones):
    primary_turn = True
    continue_game = True
    while continue_game:



        if stones = 0: # winning condition

        if stones < 0: # losing condition.
            pass
