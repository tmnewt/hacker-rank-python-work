# https://www.hackerrank.com/challenges/alternating-characters/problem
#
# some observations
# For a substring, AAB, it doesn't matter if you evaluated the A on the
#   0 index or the A on the 1st index. The fact is, there are consecutive A's
#
# 2 simple pattern states. This is it.
#
#   the current letter is surrounded by different letters, in which case, 
#       nothing needs to be done.
# 
#   the current letter is flanked by 1 or 2 of the same letter.
#
# so, if you aim to delete consecutive characters, then you will always achieve the
#   minimum number of deletions.

def alternatingCharacters(s:str):
    deletions = 0
    last_ch = s[0]
    for i in range(1, len(s)):
        if last_ch == s[i]:
            deletions += 1
        last_ch = s[i]
    return deletions

print(alternatingCharacters('abababbabbba'))