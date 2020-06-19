# https://www.hackerrank.com/challenges/repeated-string/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=warmup

# problem mixes string manipulation and modulo

string = 'abada'
num = 100

def repeatedStrings(s: str, n: int):
    length = len(s)
    fullOccurrence = n//length
    remainder = n%length
    aCount = 0
    for i in s:
        if i == 'a':
            aCount += 1
    # majority
    answer = aCount * fullOccurrence
    
    aCount = 0
    if remainder != 0:
        # 'tail'
        sub = s[0:remainder]
        aCount = 0
        for i in sub:
            if i == 'a':
                aCount += 1
        
    return answer + aCount

print(repeatedStrings(string, num))