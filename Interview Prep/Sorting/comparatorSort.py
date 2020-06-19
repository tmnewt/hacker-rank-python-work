# https://www.hackerrank.com/challenges/ctci-comparator-sorting/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=sorting&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

# Given an array of n Player objects, write an comparator that sorts them
# in order of decreasing score. If 2 or more players have the same score
# sort those players alphabetically ascending by name.
# 
# Additionally, the comparator function returns -1 is a < b, 
# 0 if a = b, and 1 if a > b  #

from functools import cmp_to_key
class Player:
    def __init__(self, name: str, score: int):
        self.name = name
        self.score = score

    def __repr__(self):
        pass
        
    def comparator(a, b):
        if a.score > b.score:
            return -1
        if a.score < b.score:
            return 1
        if a.name < b.name:
            return -1
        if a.name > b.name:
            return 1
        return 0



