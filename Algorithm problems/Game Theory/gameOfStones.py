# https://www.hackerrank.com/challenges/game-of-stones-1/problem
#
# P1 always goes first. 
# Players may take 2, 3, or 5 stones.
# If a player is unable to make a move, they lose. Simply put, if the number of stones on your turn is 1 or 0 you lose. Conversley, if you take the last stones you win (because your opponent can't move)
#
# Typically, these games follow a pattern where the starting amount and who moves first matters.
# 
# In on instance, players where allowed to take anywhere between 1 and 4 stones. In that game, the winner was determined if they could end their turn with the pile being 
# some multiple of 4 + 1

# 
# Obviously 2, 3, or 5 stones on YOUR turn means you win. and that extends to all these numbers + 1 because...
#       At 6 take 5 and they lose
#       At 5 take 5 and they lose
#       At 4 take 3 ....
#       etc.
#
#  what about at higher numbers?
#
# At 7 (lose if receiving, win if giving)
#       take 5, they take 2, you lose
#       take 3, they take 3, there is 1 left, you lose
#       take 2, they take 5, you lose.
#
# At 8 (lose if receiving, win if giving)
#       take 5, they take 3, you lose
#       take 3, they take 5, you lose
#       take 2, they take 5, you lose
# 
# AT 9  (win by taking 2)
#       take 5, they take 3, you lose
#       take 3, they take 5, you lose with 1 stone left.
#       take 2, you win
#
# at 10, (win by taking 2 or 3)
#       take 5, they take 5, you lose on 0
#       take 3, you win
#       take 2, you win 
#
# at 11 (win by taking 3)
#       take 5, they take 5, you lose on 1
#       take 3, you win
#       take 2, they take 2, you lose on 7
# 
# at 12 (win by taking 5)
#       take 5, you win
#       take 3, they take 2, you lose on 7
#       take 2, they take 3, you lose on 7 (or they take 2, you lose on 8)
# 
# at 13 (win by taking 5)
#       take 5, you win
#       take 3, they take 3, you lose on 7
#       take 2, they take 3, you lose on 8
# 
# at 14 (lose if receiving, win if giving)
#       take 5, they take 2, you lose on 7
#       take 3, they take 3, you lose on 8
#       take 2, they take 5, you lose on 7
# 
# at 15 (lose if receiving, win if giving)
#       take 5, they take 3, you lose on 7
#       take 3, they take 5, you lose on 7
#       take 2, they take 5, you lose on 8
# 
# at 16 (win by taking 2)
#       take 5, they take 3, you lose on 8
#       take 3, they take 5, you lose on 8
#       take 2, you win on 14
# 
# at 17 (win by taking 2 or 3)
#       take 5, they take 5, you lose on 7
#       take 3, you win on 14
#       take 2, you win on 15
# 
# at 18 (win by taking 3)
#       take 5, they take 5, you lose on 8
#       take 3, you win on 15
#       take 2, they take 2, you lose on 14
#
# at 19 (win by taking 5)
#       take 5, you win on 14
#       take 3, they take 2, you lose on 14
#       take 2, they take 3, you lose on 14 (or they take 2, you lose on 15)
# 
# at 20 (win by taking 5)
#       take 5, you win on 15
#       take 3, they take 3, you lose on 14
#       take 2, they take 3, you lose on 15
# 
# at 21 (lose if receiving, win if giving)
#       take 5, they take 2, you lose on 14
#       take 3, they take 3, you lose on 15
#       take 2, they take 5, you lose on 14
# 
# at 22 (lose if receiving, win if giving)
#       take 5, they take 3, you lose on 14
#       take 3, they take 5, you lose on 14
#       take 2, they take 5, you lose on 15

# ok, it is pretty obvious the pattern.  You lose on 0,1 and multiples of 7 and multiples of 7 + 1   (not multiples of 8 !!)

def gameOfStones(stone):
    if stone in [2, 3, 4, 5, 6]:
        return 'First'
    if stone%7 in [0, 1]:
        return 'Second'
    return 'First'