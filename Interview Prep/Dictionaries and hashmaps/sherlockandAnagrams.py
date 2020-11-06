# https://www.hackerrank.com/challenges/sherlock-and-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps&h_r=next-challenge&h_v=zen
# Given a string, find the number of pairs of substrings of the string that are anagrams of each other. 
#
# for instance, [ i  f  a  i  l  u  h  k  q  q ]
# using * we will mark which characters an anagram draws from:
#   [ i  f  a  i  l  u  h  k  q  q ]  --> []   :   []  <-- [ i  f  a  i  l  u  h  k  q  q ]
#1. [(i  f  a) i  l  u  h  k  q  q ]  --> [ifa]:[fai]  <-- [ i (f  a  i) l  u  h  k  q  q ]
#2. [(i) f  a  i  l  u  h  k  q  q ]  --> [i]  :  [i]  <-- [ i  f  a (i) l  u  h  k  q  q ]
#3. [ i  f  a  i  l  u  h  k (q) q ]  --> [q]  :  [q]  <-- [ i  f  a  i  l  u  h  k  q (q)]
# So the above string has 3 anagrammatic pairs.

# another one,  [ a  b  b  a ]
#  [ a  b  b  a ] --> []    :    [] <-- [ a  b  b  a ]
#1.[(a) b  b  a ] --> [a]   :   [a] <-- [ a  b  b (a)]
#2.[ a (b) b  a ] --> [b]   :   [b] <-- [ a  b (b) a ]
#3.[(a  b) b  a ] --> [ab]  :  [ba] <-- [ a  b (b  a)]
#4.[(a  b  b) a ] --> [abb] : [bba] <-- [ a (b  b  a)]

# One more,     [ a  b  b  a  a ]
#    [ a  b  b  a  a ] -->  []     :      []  <-- [ a  b  b  a  a ]
#1.  [(a) b  b  a  a ] -->  [a]    :     [a]  <-- [ a  b  b (a) a ]
#2.  [(a) b  b  a  a ] -->  [a]    :     [a]  <-- [ a  b  b  a (a)]
#3.  [ a  b  b (a) a ] -->  [a]    :     [a]  <-- [ a  b  b  a (a)]
#    ...

# The rest are the same as [a b b a] from earlier

# couple things of note:
# anagrams must be a continuous group. That means, no disjunct grabing of letters.
# A single character anagram pair of (a1, a2) is the same as (a2, a1). Thus there is only 1 pair here.
# For multi character anagram pairs found within [abbabb] the pair {(a1,b2,b3) , (b2,b3,a4)} is the same as {(b2,b3,a4), (a1,b2,b3)}
# this means there is no need to look backwards. Iterating forward and storing with dictionaries will be sufficient.
# from a given index look all the way to the end and take that slice as the substring. 
# Then sort that substring.
# Check if the substring matches anything in the dictionary.
#   If it does, increment the count of that substring.
#   If not, store the substring as a new key in the dictionary.
# To avoid double counting substring occurrences use:  
#       
#       (c(substring) * (c(substring) - 1)) // 2
#    
#   Where c() is the function of choice to count the substring occurrences.

def sherlockAndAnagrams(string):
    pairs = 0
    sub_string_dictionary = dict()
    for i in range(len(string)):
        for j in range(i, len(string)):
            sub_string = ''.join(sorted(string[ i : j+1]))
            print(sub_string)
            try:
                sub_string_dictionary[sub_string] += 1
            except KeyError:
                sub_string_dictionary[sub_string] = 1
    for key, count in sub_string_dictionary.items():
        if count > 1:
            pairs += (count*(count-1))//2
    return pairs

test = 'xyyx'
print(sherlockAndAnagrams(test))
print(sherlockAndAnagrams('abbaa'))

            















# something unrelated

#def getprimes(x):
#    primes = []
#    for a in range(1, 10000):
#        for b in range(2, a):
#            if a % b == 0:
#                break
#        else:
#            primes.append(a)    
#        if len(primes) == x:
#            return primes
#
#values = getprimes(26)
#print(ascii_lowercase)
#dic = dict(zip(ascii_lowercase, values))
#print(dic)