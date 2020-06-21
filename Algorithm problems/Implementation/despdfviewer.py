# https://www.hackerrank.com/challenges/designer-pdf-viewer/problem?h_r=internal-search

def designerPdfViewer(h: list, word: str):
    base = len(word)
    abc = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'.split()
    pair = dict(zip(abc, h))
    height = 1
    for letter in word:
        if pair[letter] > height:
            height = pair[letter]
    return base*height

#abc = 'a b c d e f g h i j k l m n o p q r s t u v w x y z'
lineIn = '1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5'
test = list(map(int, lineIn.rstrip().split()))
#abc = abc.split()
#print(abc)
#print(test)
#combo = dict(zip(abc, test))
#print(combo['b'])

print(designerPdfViewer(test, 'abc'))
