# https://www.hackerrank.com/challenges/ctci-ransom-note/problem?h_l=interview&playlist_slugs%5B%5D=interview-preparation-kit&playlist_slugs%5B%5D=dictionaries-hashmaps
# The easiest solution is utilize the counter object from the collections package.
# Don't know what I am talking about? Check out this first: https://www.hackerrank.com/challenges/collections-counter/problem
# Also go to this https://docs.python.org/3/library/collections.html#collections.Counter
# Now that you know that, you are done



from collections import Counter

def checkMagazine(magazine, note):
    magazine_count_container = Counter(magazine)
    note_count_container = Counter(note)
    magazine_count_container.subtract(note_count_container)
    deficit = -magazine_count_container
    if len(deficit) > 0:
        print('No')
    else:
        print('Yes')


mag_test  = "Ive got a lovely bunch of coconuts".split()
note_test = "ive got coconuts".split()

checkMagazine(mag_test, note_test)