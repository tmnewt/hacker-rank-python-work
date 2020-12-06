# https://www.hackerrank.com/challenges/abbr/problem
# It's insanely easy to determine if a string cannot be abbreviated. It's hard to prove the opposite...
# Only the following operations are allowed on a given string
#
#   1. Capitalize zero or more of the string's lowercase letters
#   2. Delete all of the remaining lowercase letters in the given string.
#
# Following these rules, given the string "AbcDE" can the operations reach the string "ABDE" ?
#       Here, yes, it can. Switch b to B, and discard c.
#
# Given "abcDE" can "AFDE" be reached? No, because F never occurred in the first place. We 
#       cannot add letters, only remove (lowercase) letters.
#
# Given "aBcDE" can "ADE" be  reached? No, because we can't remove B because it is capitalized.
#
# 
#
# Consider this example:
#
#   Can "websitEsdontenDONjunktrypyThonworksdoTcom"  be abbreviated as "WEDONTWORKDOTCOM" ??? YES
# 
#   We can see that this example contains lowercase letters that do not need to be used, specifically,
#
#       "websitEsdontenDONjunktrypyThonworksdoTcom"
#                ^^^^
#                these letters which make up the word 'DONT' must NOT be used otherwise the abbreviation
#                cannot be built.
#       
#   So the best thing to do is read up to the next Capital letter. Everything before it forms a pool.
#   The first capital letter is E
#   so the pool of letters before it are 'w e b s i t'.
#   Now look at the abbreviation. Get the index of the first occurrence of 'E' within the abbreviation.
#   Are there any other capital letters preceding it in the abbreviation? Yes, 'W'.
#   Check lowercase pool for 'w'. If it's not there, then the abbreviation can't be built.
#   Here, though, 'w' is in the pool. Pop off the letters "WE" from the abbreviation (or mark them somehow.)





# Consider another example with the same given string but a different abbreviation
#
#   Can "websitEsdontenDONjunkTrypyThonworksdoTcom"  be abbreviated as "WEDONTDONTWORKDOTCOM" ??? NO

# consider this example:
#
#   Can 'dontDontdONTDont be abbreviated as 'DONTDONTDONTDONT' ??? YES