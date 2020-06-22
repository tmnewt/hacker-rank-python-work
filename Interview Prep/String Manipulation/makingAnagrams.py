# https://www.hackerrank.com/challenges/ctci-making-anagrams/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=strings

testA = 'abcdddeefggggggbalsss'
testB = 'abdcdedfeggggggbjlss'

def makeAnagram(a: str, b: str):
    a = list(a)
    b = list(b)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
               'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 
               'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    gramA = {k:0 for k in letters}
    gramB = {k:0 for k in letters}

    for i in a:
        gramA[i] += 1
    for i in b:
        gramB[i] += 1
    #print(gramA)
    #print(gramB)

    gramDiff = 0
    for key in letters:
        gramDiff += (abs(gramA[key]-gramB[key]))

    return gramDiff

print(makeAnagram(testA, testB))

