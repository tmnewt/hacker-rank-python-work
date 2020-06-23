# https://www.hackerrank.com/challenges/the-minion-game/problem?h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

def minion_game(string: str):
    vowels = 'A E I O U'.split()
    stuart = 0; kevin = 0
    for i in range(len(string)):
        indexscore = len(string)-i
        if string[i] in vowels:
            kevin += indexscore
        else:
            stuart += indexscore
    if kevin == stuart: 
        print('Draw')
    elif kevin > stuart:
        print(f'Kevin {kevin}')
    else:
        print(f'Stuart {stuart}')

minion_game('BANANA')
   

# this problem can be tackled by thinking about the number of substrings that can be formed
# from a given index and then correctly assigning the score. 

# suppose the following.
# loop over the primary string one element at a time and count the number of substrings 
# we could create from THAT index


# Using the string '
# for instance: string[0] would equal 'B'
# there are 6 substrings that can be created from this index.
#       BANANA
#       BANAN
#       BANA
#       BAN
#       BA
#       B
# that gives a score of 6 and would go to player 1 because B is a consonant
# keep in mind we didn't go searching for those substrings. It simply logically follows that
# any letters after the index would be part of the substring.

# next, string[1] would equal 'A'
# rather than go searching for all substrings follow the same approach as above.
#       ANANA
#       ANAN
#       ANA
#       AN
#       A
# which gives a score of 5 which goes to player 2 because A is a vowel.

# But on the problem A appears 3 times! We are missing those, right?  Actually we will 
# still get those. Lets keep up this pattern 
# 
# if we keep this process up then the next step would be string[2] which is 'N'
#       NANA
#       NAN
#       NA
#       N
#that gives a score of 4 and would go to player 1 because N is a consonant

# you might start noticing a pattern here. incrementing 1 step at a time and distributing the
# score to right player is much faster than searching through a string.

# as for the score to distribute at each step, it can be calculated as the difference between the
# current index and the end of the string, or len(string)- i

# this saves a ton of heavy lifting and means the only thing required is figuring out which
# player to distribute the score to.